import configparser
import os


class Constantes:
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

    # (Soporte) Detalles de web scraping
    lk = config.get("links", "base_url", fallback="")
    wr = config.get("links", "path_wr", fallback="")
    cs = config.get("links", "path_cs", fallback="")
    en = config.get("links", "path_en", fallback="")
    base = config.get("subject-params", "base", fallback="")
    scrs = config.get("subject-params", "scrs", fallback="")
    stts = config.get("subject-params", "stts", fallback="")
    # (Soporte) Campos para scores, detalles y stats
    scrs_titles_str = config.get("scrs", "scrs_titles", fallback="")
    scrs_ws_wr_str = config.get("scrs", "scrs_ws_wr", fallback="")
    scrs_ws_su_str = config.get("scrs", "scrs_ws_su", fallback="")
    stts_titles_str = config.get("stts", "stts_titles", fallback="")
    stts_ws_wr_str = config.get("stts", "stts_ws_wr", fallback="")
    stts_ws_su_str = config.get("stts", "stts_ws_su", fallback="")

    # Construcción de links para web scraping
    lk_wr = f"{lk}/{wr}"
    lk_cs_scrs = f"{lk}/{cs}{base}/{scrs}"
    lk_en_scrs = f"{lk}/{en}{base}/{scrs}"
    lk_cs_stts = f"{lk}/{cs}{base}/{stts}"
    lk_en_stts = f"{lk}/{en}{base}/{stts}"
    # Construcción de columnas y campos de extracción
    scores_titles = [s.strip() for s in scrs_titles_str.split(",") if s.strip()]
    scores_ws_wr = [s.strip() for s in scrs_ws_wr_str.split(",") if s.strip()]
    scores_ws_su = [s.strip() for s in scrs_ws_su_str.split(",") if s.strip()]
    # details_titles = [s.strip() for s in details_titles_str.split(",") if s.strip()]
    stats_titles = [s.strip() for s in stts_titles_str.split(",") if s.strip()]
    stats_ws_wr = [s.strip() for s in stts_ws_wr_str.split(",") if s.strip()]
    stats_ws_su = [s.strip() for s in stts_ws_su_str.split(",") if s.strip()]
