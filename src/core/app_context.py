from dataclasses import dataclass
from pathlib import Path

from src.app import config as cfg
from src.app import paths as p
from src.app import runtime_paths as rp

@dataclass(frozen=True)
class AppConfig:
    app_size: str
    app_title: str
    app_id: str
    app_url_api: str
    app_token_api: str

@dataclass(frozen=True)
class AppPaths:
    project_dir: Path
    src_dir: Path
    assets_dir: Path
    icon_dir: Path
    img_dir: Path
    templates_dir: Path

@dataclass(frozen=True)
class AppRuntimePaths:
    data_dir: Path
    logs_dir: Path
    templates_dir: Path
    consultar_readme_file: Path

@dataclass(frozen=True)
class AppContext:
    config: AppConfig
    paths: AppPaths
    runtime: AppRuntimePaths

def build_app_context() -> AppContext:
    return AppContext(
        config = AppConfig(
            app_size=cfg.APP_SIZE,
            app_title=cfg.APP_TITLE,
            app_id=cfg.APP_ID,
            app_url_api=cfg.APP_URL_API,
            app_token_api=cfg.APP_TOKEN_API,
        ),
        paths = AppPaths(
            project_dir=p.PROJECT_DIR,
            src_dir=p.SRC_DIR,
            assets_dir=p.ASSETS_DIR,
            icon_dir=p.ICON_DIR,
            img_dir=p.IMG_DIR,
            templates_dir=p.TEMPLATES_DIR,
        ),
        runtime = AppRuntimePaths(
            data_dir=rp.DATA_DIR,
            logs_dir=rp.LOGS_DIR,
            templates_dir=rp.TEMPLATE_DIR,
            consultar_readme_file=rp.CONSULTAR_README_FILE,
        ),
    )