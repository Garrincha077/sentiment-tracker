from __future__ import annotations

from dataclasses import dataclass

MODEL_VERSION = "v0.9.1-RSI-ICI132"
PAPER_STRATEGY_VERSION = "v0.8-paper"

FINAL_WEIGHTS = {
    "core_greed": 0.72,
    "dxy_pressure": 0.09,
    "cot_crowding": 0.09,
    "spy_rsi_14": 0.10,
}

LEAF_WEIGHTS = {
    "vix_level": 0.0864,
    "equity_put_call_daily": 0.0432,
    "total_put_call_10d": 0.0720,
    "vix_term_structure": 0.0504,
    "naaim_exposure": 0.0864,
    "aaii_bull_bear": 0.0576,
    "ici_weekly_equity_flows": 0.0720,
    "market_breadth": 0.0864,
    "hy_oas": 0.0360,
    "hyg_ief": 0.0216,
    "insider_activity": 0.0720,
    "cnn_fear_greed": 0.0360,
    "dxy_30w_slope": 0.0450,
    "dxy_ema_cross": 0.0450,
    "cot_large_specs": 0.0378,
    "cot_commercials_inverted": 0.0360,
    "cot_small_specs": 0.0162,
    "spy_rsi_14": 0.1000,
}

SIGNAL_THRESHOLDS = {
    "extreme_fear": 20.0,
    "fear": 35.0,
    "greed": 65.0,
    "extreme_greed": 80.0,
}

CONFIDENCE_WEIGHTS = {
    "coverage": 0.40,
    "freshness": 0.25,
    "agreement": 0.25,
    "source_quality": 0.10,
}

COT_HORIZON_WEIGHTS = {"26w": 0.50, "52w": 0.30, "156w": 0.20}


@dataclass(frozen=True)
class ConfigValidation:
    final_weight_total: float
    leaf_weight_total: float
    valid: bool


def validate_configuration() -> ConfigValidation:
    final_total = sum(FINAL_WEIGHTS.values())
    leaf_total = sum(LEAF_WEIGHTS.values())
    return ConfigValidation(
        final_weight_total=final_total,
        leaf_weight_total=leaf_total,
        valid=abs(final_total - 1.0) < 1e-9 and abs(leaf_total - 1.0) < 1e-9,
    )
