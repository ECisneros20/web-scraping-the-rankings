import logging
from urllib.request import urlopen

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as soup
from selenium import webdriver

from log import setup_logging
from utils.constantes import Constantes

# Configura el logging
setup_logging()
# Obtiene un logger para este módulo
logger = logging.getLogger(__name__)


# Ruta del archivo log
archivo_log = f"{Constantes.ruta_log.value}/app.log"
logger = SimpleLogger(file_name=archivo_log, log_name="the_ranking", level=logging.INFO)


if __name__ == "__main__":
    for ranking_name, link in Constantes.ranking_links.value.items():
        cantidad_filas = -1

        # Links para queries
        link_ranking = f"{link}#!/length/-1/sort_by/rank/sort_order/asc/cols/stats"
        link_scores = f"{link}#!/length/-1/sort_by/rank/sort_order/asc/cols/scores"

        # Dos objetos tipo webdriver, uno para cada link
        ranking_browser = webdriver.Chrome()
        scores_browser = webdriver.Chrome()

        # Usar el webdriver para un request al link
        ranking_browser.get(link_ranking)
        # Obtener el html del link una vez cargado
        ranking_page_html = ranking_browser.page_source
        # Parse el HTML con BeautifulSoup
        ranking_page_soup = soup(ranking_page_html, "html.parser")
        # Generar una lista por cada columna de la tabla
        ranking_obj = []
        for title_name in Constantes.ranking_ws.value:
            ranking_obj.append(ranking_page_soup.findAll("td", {"class": title_name}))
        # Cerrar el browser
        ranking_browser.close()

        # Usar el webdriver para un request al link
        scores_browser.get(link_scores)
        # Obtener el html del link una vez cargado
        scores_page_html = scores_browser.page_source
        # Parse el HTML con BeautifulSoup
        scores_page_soup = soup(scores_page_html, "html.parser")
        # Generar una lista por cada columna de la tabla
        scores_obj = []
        for title_name in Constantes.scores_ws.value:
            scores_obj.append(scores_page_soup.findAll("td", {"class": title_name}))
        # Cerrar el browser
        scores_browser.close()

        # Para construir la información del ranking
        ranking = []
        nombres_universidad = []
        link_universidades = []
        cantidad_estudiantes = []
        proporcion_estudiantes_staff = []
        cantidad_estudiantes_internacionales = []
        ratio_mujeres_hombres = []
        porcentaje_investigacion_interdisciplinaria = []
        # Para construir la información de scores
        overall_score = []
        teaching_score = []
        research_score = []
        citations_score = []
        industry_income_score = []
        international_outlook_score = []
        # Reconstruir información sobre cada fila
        count_universidades = 0
        for pos, _ in enumerate(nombres_universidad_obj):
            count_universidades += 1
            if count_universidades > cantidad_universidades:
                break
            ranking.append(ranking_obj[pos].text)
            # Extraer solo nombre de la universidad o un link con más información
            try:
                nombres_universidad.append(nombres_universidad_obj[pos].a.text)
            except Exception as e:
                print(f"El nombre de la universidad no es solo texto: {e}")
                nombres_universidad.append(
                    nombres_universidad_obj[pos]
                    .findAll("div", {"class": "ranking-institution-title"})[0]
                    .text
                )
            # Extraer la información del link que tal vez se obtuvo en la parte anterior
            try:
                link_universidades.append(
                    "https://www.timeshighereducation.com"
                    + nombres_universidad_obj[pos].a.get("href")
                )
            except Exception as e:
                print(f"No hay un link para poder aplicar web scraping: {e}")
                link_universidades.append("")
            cantidad_estudiantes.append(cantidad_estudiantes_obj[pos].text)
            proporcion_estudiantes_staff.append(
                proporcion_estudiantes_staff_obj[pos].text
            )
            cantidad_estudiantes_internacionales.append(
                cantidad_estudiantes_internacionales_obj[pos].text
            )
            ratio_mujeres_hombres.append(ratio_mujeres_hombres_obj[pos].text)
            if len(porcentaje_investigacion_interdisciplinaria_obj) != 0:
                porcentaje_investigacion_interdisciplinaria.append(
                    porcentaje_investigacion_interdisciplinaria_obj[pos].text
                )

            overall_score.append(overall_score_obj[pos].text)
            teaching_score.append(teaching_score_obj[pos].text)
            research_score.append(research_score_obj[pos].text)
            citations_score.append(citations_score_obj[pos].text)
            industry_income_score.append(industry_income_score_obj[pos].text)
            international_outlook_score.append(
                international_outlook_score_obj[pos].text
            )

        (
            full_address_list,
            streetAddress_list,
            addressLocality_list,
            addressRegion_list,
            postalCode_list,
            addressCountry_list,
        ) = [], [], [], [], [], []
        count_universidades = 0
        for web in link_universidades:
            count_universidades += 1
            if count_universidades > cantidad_universidades:
                break

            if web != "":
                page = urlopen(web)
                page_html = soup(page, "html.parser")

                full_address = page_html.findAll(
                    "div",
                    {
                        "class": "institution-info__contact-detail institution-info__contact-detail--address"
                    },
                )[0].text.strip()
                full_address_list.append(full_address)

                if len(full_address.split(", ")) == 1:
                    streetAddress_list.append("Sin dirección")
                    addressLocality_list.append("Sin dirección")
                    addressRegion_list.append("Sin dirección")
                    postalCode_list.append("Sin código postal")
                    addressCountry_list.append(full_address.split(", ")[0])
                    print(
                        f"{len(full_address_list)} out of {len(link_universidades)} - {full_address}"
                    )
                elif len(full_address.split(", ")) == 2:
                    streetAddress_list.append("Sin dirección")
                    addressLocality_list.append("Sin dirección")
                    addressRegion_list.append(full_address.split(", ")[0])
                    postalCode_list.append("Sin código postal")
                    addressCountry_list.append(full_address.split(", ")[1])
                    print(
                        f"{len(full_address_list)} out of {len(link_universidades)} - {full_address}"
                    )
                elif len(full_address.split(", ")) == 3:
                    streetAddress_list.append("Sin dirección")
                    addressLocality_list.append(full_address.split(", ")[0])
                    addressRegion_list.append(full_address.split(", ")[1])
                    postalCode_list.append("Sin código postal")
                    addressCountry_list.append(full_address.split(", ")[2])
                    print(
                        f"{len(full_address_list)} out of {len(link_universidades)} - {full_address}"
                    )
                elif len(full_address.split(", ")) == 4:
                    streetAddress_list.append("Sin dirección")
                    addressLocality_list.append(full_address.split(", ")[0])
                    addressRegion_list.append(full_address.split(", ")[1])
                    postalCode_list.append(full_address.split(", ")[2])
                    addressCountry_list.append(full_address.split(", ")[3])
                    print(
                        f"{len(full_address_list)} out of {len(link_universidades)} - {full_address}"
                    )
                elif len(full_address.split(", ")) == 5:
                    streetAddress_list.append(full_address.split(", ")[0])
                    addressLocality_list.append(full_address.split(", ")[1])
                    addressRegion_list.append(full_address.split(", ")[2])
                    postalCode_list.append(full_address.split(", ")[3])
                    addressCountry_list.append(full_address.split(", ")[4])
                    print(
                        f"{len(full_address_list)} out of {len(link_universidades)} - {full_address}"
                    )
                elif len(full_address.split(", ")) == 6:
                    streetAddress_list.append(", ".join(full_address.split(", ")[0:2]))
                    addressLocality_list.append(full_address.split(", ")[2])
                    addressRegion_list.append(full_address.split(", ")[3])
                    postalCode_list.append(full_address.split(", ")[4])
                    addressCountry_list.append(full_address.split(", ")[5])
                    print(
                        f"{len(full_address_list)} out of {len(link_universidades)} - {full_address}"
                    )
                elif len(full_address.split(", ")) == 7:
                    streetAddress_list.append(", ".join(full_address.split(", ")[0:3]))
                    addressLocality_list.append(full_address.split(", ")[3])
                    addressRegion_list.append(full_address.split(", ")[4])
                    postalCode_list.append(full_address.split(", ")[5])
                    addressCountry_list.append(full_address.split(", ")[6])
                    print(
                        f"{len(full_address_list)} out of {len(link_universidades)} - {full_address}"
                    )
                else:
                    streetAddress_list.append("Demasiados valores para procesar")
                    addressLocality_list.append("Demasiados valores para procesar")
                    addressRegion_list.append("Demasiados valores para procesar")
                    postalCode_list.append("Demasiados valores para procesar")
                    addressCountry_list.append("Demasiados valores para procesar")
                    print(
                        f"{len(full_address_list)} out of {len(link_universidades)} - Problemas - {full_address} - {len(full_address.split(', '))}"
                    )
            else:
                full_address_list.append("Sin link")
                streetAddress_list.append("Sin link")
                addressLocality_list.append("Sin link")
                addressRegion_list.append("Sin link")
                postalCode_list.append("Sin link")
                addressCountry_list.append("Sin link")
                print(
                    f"{len(full_address_list)} out of {len(link_universidades)} - Sin link"
                )

        if len(porcentaje_investigacion_interdisciplinaria_obj) != 0:
            df = pd.DataFrame(
                {
                    "rank": ranking,
                    "name": nombres_universidad,
                    "number_students": cantidad_estudiantes,
                    "student_staff_ratio": proporcion_estudiantes_staff,
                    "intl_students": cantidad_estudiantes_internacionales,
                    "female_male_ratio": ratio_mujeres_hombres,
                    "%_interdisc_science_research": porcentaje_investigacion_interdisciplinaria,
                    "overall_score": overall_score,
                    "teaching_score": teaching_score,
                    "research_score": research_score,
                    "citations_score": citations_score,
                    "industry_income_score": industry_income_score,
                    "international_outlook_score": international_outlook_score,
                    "address": full_address_list,
                    "street_address": streetAddress_list,
                    "locality_address": addressLocality_list,
                    "region_address": addressRegion_list,
                    "postcode_address": postalCode_list,
                    "country_address": addressCountry_list,
                }
            )

        else:
            df = pd.DataFrame(
                {
                    "rank": ranking,
                    "name": nombres_universidad,
                    "number_students": cantidad_estudiantes,
                    "student_staff_ratio": proporcion_estudiantes_staff,
                    "intl_students": cantidad_estudiantes_internacionales,
                    "female_male_ratio": ratio_mujeres_hombres,
                    "overall_score": overall_score,
                    "teaching_score": teaching_score,
                    "research_score": research_score,
                    "citations_score": citations_score,
                    "industry_income_score": industry_income_score,
                    "international_outlook_score": international_outlook_score,
                    "address": full_address_list,
                    "street_address": streetAddress_list,
                    "locality_address": addressLocality_list,
                    "region_address": addressRegion_list,
                    "postcode_address": postalCode_list,
                    "country_address": addressCountry_list,
                }
            )

        df["number_students"] = df["number_students"].str.replace(
            pat=",", repl="", regex=True
        )
        df = df.replace("n/a*", np.nan, regex=True)
        df.to_csv(f"ranking_the_{tipo_ranking}.csv", encoding="utf-16", index=False)

        print("Programa terminado, cierre el programa . . .")
