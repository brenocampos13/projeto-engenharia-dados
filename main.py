from etl.oltp_raw.clientes import pipeline_oltp_raw_clientes
from etl.oltp_raw.clinicas import pipeline_oltp_raw_clinicas
from etl.oltp_raw.origens import pipeline_oltp_raw_origens
from etl.oltp_raw.produtos import pipeline_oltp_raw_produtos
from etl.oltp_raw.vendas import pipeline_oltp_raw_vendas

from etl.raw_staging.clientes import pipeline_raw_staging_clientes
from etl.raw_staging.clinicas import pipeline_raw_staging_clinicas
from etl.raw_staging.origens import pipeline_raw_staging_origens
from etl.raw_staging.produtos import pipeline_raw_staging_produtos
from etl.raw_staging.vendas import pipeline_raw_staging_vendas

from etl.staging_analytics.clientes import pipeline_staging_analytics_clientes
from etl.staging_analytics.clinicas import pipeline_staging_analytics_clinicas
from etl.staging_analytics.origens import pipeline_staging_analytics_origens
from etl.staging_analytics.produtos import pipeline_staging_analytics_produtos
from etl.staging_analytics.vendas import pipeline_staging_analytics_vendas

if __name__ == "__main__":
    pipeline_oltp_raw_clientes()
    pipeline_oltp_raw_clinicas()
    pipeline_oltp_raw_origens()
    pipeline_oltp_raw_produtos()
    pipeline_oltp_raw_vendas()

    pipeline_raw_staging_clientes()
    pipeline_raw_staging_clinicas()
    pipeline_raw_staging_origens()
    pipeline_raw_staging_produtos()
    pipeline_raw_staging_vendas()

    pipeline_staging_analytics_clientes()
    pipeline_staging_analytics_clinicas()
    pipeline_staging_analytics_origens()
    pipeline_staging_analytics_produtos()
    pipeline_staging_analytics_vendas()