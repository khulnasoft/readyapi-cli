import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import uvicorn
from readyapi_cli.cli import app
from typer.testing import CliRunner

from tests.utils import changing_dir

runner = CliRunner()
assets_path = Path(__file__).parent / "assets"

def test_dev() -> None:
    with changing_dir(assets_path):
        with patch.object(uvicorn, "run") as mock_run:
            result = runner.invoke(app, ["dev", "single_file_app.py"])
            assert result.exit_code == 0, result.output
            assert mock_run.called
            assert mock_run.call_args
            assert mock_run.call_args.kwargs == {
                "app": "single_file_app:app",
                "host": "127.0.0.1",
                "port": 8000,
                "reload": True,
                "workers": None,
                "root_path": "",
                "proxy_headers": True,
            }
        # Debug print the actual output
        print("Actual output:", result.output)
        
        # Analyze and adjust assertions
        assert "Using import string single_file_app:app" in result.output
        
        # Checking for more flexible parts of the output
        dev_mode_header = "ReadyAPI CLI - Development mode"
        assert dev_mode_header in result.output, f"Header '{dev_mode_header}' not found in output"
        
        assert "│  Serving at: http://127.0.0.1:8000" in result.output
        assert "│  API docs: http://127.0.0.1:8000/docs" in result.output
        assert "│  Running in development mode, for production use:" in result.output
        assert "│  readyapi run" in result.output

# Example usage of the adjusted function:
if __name__ == "__main__":
    test_dev()
