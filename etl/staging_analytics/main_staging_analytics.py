from etl.staging_analytics.clientes import pipeline_staging_analytics_clientes
from etl.staging_analytics.clinicas import pipeline_staging_analytics_clinicas
from etl.staging_analytics.origens import pipeline_staging_analytics_origens
from etl.staging_analytics.produtos import pipeline_staging_analytics_produtos
from etl.staging_analytics.vendas import pipeline_staging_analytics_vendas

def pipeline_staging_analytics():
    pipeline_staging_analytics_produtos()
    pipeline_staging_analytics_clientes()
    pipeline_staging_analytics_clinicas()
    pipeline_staging_analytics_origens()
    pipeline_staging_analytics_vendas()

if __name__ == "__main__":
    pipeline_staging_analytics()
