from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_env_is_gitignored():
    lines = (ROOT / ".gitignore").read_text().splitlines()
    assert ".env" in lines


def test_env_example_has_required_keys():
    text = (ROOT / ".env.example").read_text()
    for key in ("OPENAI_API_KEY", "LLM_MODEL"):
        assert f"{key}=" in text


def test_env_example_has_no_real_key():
    for line in (ROOT / ".env.example").read_text().splitlines():
        if line.startswith("OPENAI_API_KEY="):
            assert line == "OPENAI_API_KEY="
