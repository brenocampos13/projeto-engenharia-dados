from etl.raw_staging.clientes import pipeline_raw_staging_clientes
from etl.raw_staging.clinicas import pipeline_raw_staging_clinicas
from etl.raw_staging.origens import pipeline_raw_staging_origens
from etl.raw_staging.produtos import pipeline_raw_staging_produtos
from etl.raw_staging.vendas import pipeline_raw_staging_vendas

def pipeline_raw_staging():
    pipeline_raw_staging_clientes()
    pipeline_raw_staging_clinicas()
    pipeline_raw_staging_origens()
    pipeline_raw_staging_produtos()
    pipeline_raw_staging_vendas()