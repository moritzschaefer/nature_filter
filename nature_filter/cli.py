"""Console script for nature_filter."""
import sys

import click
from flask import Flask, Response

from .nature_filter import nature_filter

PORT=9999

app = Flask(__name__)

@app.route("/nature_filter.xml", methods=['GET'])
def serve_filtered_flask():
    return Response(nature_filter(), mimetype='application/rss+xml')


@click.command()
def main(args=None):
    """Console script for nature_filter."""

    app.run(host="0.0.0.0", port=PORT)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
