import configparser
import os
from enum import Enum, unique


@unique
class Constantes(Enum):
    """Una clase que contiene constantes base del sistema, así como la
    ruta principal y de los subdirectorios del proyecto para desarrollo
    y producción.
    """

    # Encoding para editar y crear archivos txt y csv
    encoding = "utf-8"
    # Ruta principal del proyecto
    ruta_principal = os.path.dirname(os.path.dirname(__file__)).replace("\\", "/")
    # Rutas de proyecto back-end
    ruta_data = f"{ruta_principal}/data"
    ruta_log = f"{ruta_principal}/log"
    ruta_reports = f"{ruta_principal}/reports"

    # Cargar config.ini
    config = configparser.ConfigParser()
    config.read(f"{ruta_principal}/config.ini")

    # Detalles de web scraping
    lk = config.get("links", "base_url", fallback="")
    wr = config.get("links", "path_world_ranking", fallback="")
    cs = config.get("links", "path_computer_science", fallback="")
    en = config.get("links", "path_engineering", fallback="")
    base = config.get("links", "query_params_base", fallback="")
    scores = config.get("links", "query_params_scores", fallback="")
    stats = config.get("links", "query_params_stats", fallback="")
    cant_univ = config.getint("links", "cant_univ", fallback=100)
    # Construcción de links para web scraping
    lk_wr_scores = f"{lk}/{wr}{base}/{scores}"
    lk_cs_scores = f"{lk}/{cs}{base}/{scores}"
    lk_en_scores = f"{lk}/{en}{base}/{scores}"
    lk_wr_stats = f"{lk}/{wr}{base}/{stats}"
    lk_cs_stats = f"{lk}/{cs}{base}/{stats}"
    lk_en_stats = f"{lk}/{en}{base}/{stats}"

    # Campos para scores, detalles y stats
    scores_titles_str = config.get("scores", "scores_titles", fallback="")
    scores_ws_str = config.get("scores", "scores_ws", fallback="")
    details_titles_str = config.get("details", "details_titles", fallback="")
    stats_titles_str = config.get("stats", "stats_titles", fallback="")
    stats_ws_str = config.get("stats", "stats_ws", fallback="")
    # Construcción de columnas y campos de extracción
    scores_titles = [s.strip() for s in scores_titles_str.split(",") if s.strip()]
    scores_ws = [s.strip() for s in scores_ws_str.split(",") if s.strip()]
    details_titles = [s.strip() for s in details_titles_str.split(",") if s.strip()]
    stats_titles = [s.strip() for s in stats_titles_str.split(",") if s.strip()]
    stats_ws = [s.strip() for s in stats_ws_str.split(",") if s.strip()]
