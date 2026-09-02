from etl.oltp_raw.clientes import pipeline_oltp_raw_clientes
from etl.oltp_raw.clinicas import pipeline_oltp_raw_clinicas
from etl.oltp_raw.origens import pipeline_oltp_raw_origens
from etl.oltp_raw.produtos import pipeline_oltp_raw_produtos
from etl.oltp_raw.vendas import pipeline_oltp_raw_vendas

from etl.raw_staging.clientes import pipeline_raw_staging_clientes

if __name__ == "__main__":
    pipeline_oltp_raw_clientes()
    pipeline_oltp_raw_clinicas()
    pipeline_oltp_raw_origens()
    pipeline_oltp_raw_produtos()
    pipeline_oltp_raw_vendas()

    pipeline_raw_staging_clientes()