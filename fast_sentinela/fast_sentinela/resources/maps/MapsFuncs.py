import json
from functools import lru_cache
from pathlib import Path
from typing import Dict, Any, List, Optional

# Valor padrão quando as coordenadas não pertencem a nenhum estado do mapa
UNKNOWN_STATE = "DESCONHECIDO"

# Nome do arquivo GeoJSON esperado na mesma pasta deste módulo
GEOJSON_FILENAME = "map.geojson"


@lru_cache(maxsize=1)
def _load_features() -> List[Dict[str, Any]]:
    """
    Carrega as features do arquivo GeoJSON e cacheia em memória.

    O arquivo map.geojson deve estar na MESMA pasta deste arquivo.
    """
    geojson_path = Path(__file__).resolve().parent / GEOJSON_FILENAME

    if not geojson_path.exists():
        raise FileNotFoundError(
            f"Arquivo GeoJSON não encontrado em: {geojson_path}. "
            f"Coloque o arquivo '{GEOJSON_FILENAME}' na mesma pasta de map_funcs.py."
        )

    with geojson_path.open(encoding="utf-8") as f:
        data = json.load(f)

    if "features" not in data:
        raise ValueError("GeoJSON inválido: chave 'features' não encontrada.")

    return data["features"]


def _point_in_ring(x: float, y: float, ring: List[List[float]]) -> bool:
    """
    Teste de point-in-polygon em um anel (lista de [lon, lat]) usando o algoritmo de ray casting.

    x = longitude
    y = latitude
    """
    inside = False
    n = len(ring)

    for i in range(n):
        x1, y1 = ring[i - 1]
        x2, y2 = ring[i]

        # Verifica se o segmento cruza o "raio horizontal" na altura de y
        if (y1 > y) != (y2 > y):
            # Evita divisão por zero com um epsilon
            denom = (y2 - y1) if (y2 - y1) != 0 else 1e-16
            x_intersect = x1 + (x2 - x1) * (y - y1) / denom

            if x_intersect > x:
                inside = not inside

    return inside


def _point_in_polygon(x: float, y: float, coords: List[List[List[float]]]) -> bool:
    """
    Teste de point-in-polygon para um Polygon do GeoJSON.

    coords é uma lista de anéis:
      - coords[0] = anel externo
      - coords[1:], se existirem, são furos (holes)
    """
    outer = coords[0]
    holes = coords[1:]

    # Primeiro verifica se está dentro do anel externo
    if not _point_in_ring(x, y, outer):
        return False

    # Se estiver dentro do outer, verifica se cai dentro de algum "buraco"
    for hole in holes:
        if _point_in_ring(x, y, hole):
            return False

    return True


def _feature_contains_point(feature: Dict[str, Any], lat: float, lon: float) -> bool:
    """
    Verifica se o ponto (lat, lon) está dentro da geometria da feature.
    GeoJSON usa [lon, lat] nas coordenadas.
    """
    geom = feature.get("geometry") or {}
    geom_type = geom.get("type")
    coords = geom.get("coordinates")

    if not coords or not geom_type:
        return False

    x, y = lon, lat  # GeoJSON = [lon, lat]

    if geom_type == "Polygon":
        return _point_in_polygon(x, y, coords)

    if geom_type == "MultiPolygon":
        # MultiPolygon é uma lista de Polygons, cada um com seus anéis
        for poly in coords:
            if _point_in_polygon(x, y, poly):
                return True
        return False

    # Outros tipos (Point, LineString, etc.) não são tratados aqui
    return False


def find_state(latitude: float, longitude: float) -> str:
    """
    Retorna a sigla do estado (por ex. 'PE', 'AL') para as coordenadas informadas.
    Caso não encontre nenhum estado, retorna 'DESCONHECIDO'.

    :param latitude: latitude em graus (WGS84)
    :param longitude: longitude em graus (WGS84)
    """
    features = _load_features()

    for feature in features:
        if _feature_contains_point(feature, latitude, longitude):
            props = feature.get("properties") or {}
            # No teu arquivo, as chaves são: id, name, sigla
            sigla = props.get("sigla")
            if sigla:
                return sigla

    return UNKNOWN_STATE


def find_state_full_name(latitude: float, longitude: float) -> Optional[str]:
    """
    Versão alternativa que retorna o NOME completo do estado (ex.: 'PERNAMBUCO'),
    ou None se não encontrar.
    """
    features = _load_features()

    for feature in features:
        if _feature_contains_point(feature, latitude, longitude):
            props = feature.get("properties") or {}
            return props.get("name")

    return None
