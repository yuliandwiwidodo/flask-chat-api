from app import app
from app.logger import logger

# run tnc cron
@app.cli.command()
def run_tnc_cron():
    """Initialize the database."""
    logger.info(str(run_tnc))
