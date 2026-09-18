from seeds.seed_oltp import seeds_main
from etl.oltp_raw.main_oltp_raw import pipeline_oltp_raw
from etl.raw_staging.main_raw_staging import pipeline_raw_staging
from etl.staging_analytics.main_staging_analytics import pipeline_staging_analytics

if __name__ == "__main__":
    seeds_main()
    pipeline_oltp_raw()
    pipeline_raw_staging()
    pipeline_staging_analytics()