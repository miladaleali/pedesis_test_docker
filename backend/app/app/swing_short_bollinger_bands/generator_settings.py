from pedesis.components.signal_generator.templates import base_setting as base

class Logic(base.GeneratorLogicSetting):
    template_name: str = 'swing_long_bollinger_bands'
    source: str = 'close'
    bb_length: int = 20
    bb_std: int = 2
    trend_source: str = 'close'
    trend_length: int = 200
    all_indicators: list[str] = [
        'bbs',
        'trend'
    ]

    @base.cache_indicator
    def mono_calculate(
        self,
        datas: base.pd.DataFrame,
        indicator_cache_stores: dict[str, str],
        indi_name: str
    ) -> None:
        match indi_name:
            case 'bbs':
                bbs = base.pdt.bbands(
                    close=datas[self.source],
                    length=self.bb_length,
                    std=self.bb_std,
                )
                bbs.columns = ['lower', 'mid', 'upper', 'bandwidth', 'bbp']
                return bbs
            case 'trend':
                return base.calculate_ema(datas, self.trend_source, self.trend_length)


logic = Logic()

data_req = base.OhlcvStreamDataRequest(timeframe='1h')

input_ = base.GeneratorInputSetting(request=data_req)

output_settings = base.GeneratorOutputSetting(
    signal_type=base.SignalType.Long,
    analysis_style=base.AnalysisStyle.Technical,
    optimizer_tag=base.OptimizerTag.Direct,
    consumption_pattern=base.ConsumptionPattern.Disposable,
    signal_mode=base.SignalMode.Analysis,
    expire_configs=base.ExpireConfigs(
        configs={
            'timedelta': 2 * 24 * 60  # two day
        }
    )
)

Settings = base.GeneratorSettings.safe_creation(
    template_name='swing_long_bollinger_bands',
    logic=logic,
    input_=input_,
    output=output_settings
)
