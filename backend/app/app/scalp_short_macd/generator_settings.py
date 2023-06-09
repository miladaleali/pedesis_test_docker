from pedesis.components.signal_generator.templates import base_setting as base

class Logic(base.GeneratorLogicSetting):
    template_name: str = 'scalp_short_macd'
    source: str = 'close'
    fast: int = 12
    slow: int = 26
    signal: int = 9
    trend_source: str = 'close'
    trend_length: int = 100
    all_indicators: list[str] = [
        'macd',
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
            case 'macd':
                macd = base.pdt.macd(
                    close=datas[self.source],
                    fast=self.fast,
                    slow=self.slow,
                    signal=self.signal
                )
                macd.rename(
                    columns={
                        f"MACD_{self.fast}_{self.slow}_{self.signal}": 'macd',
                        f"MACDh_{self.fast}_{self.slow}_{self.signal}": 'histo',
                        f"MACDs_{self.fast}_{self.slow}_{self.signal}": 'signal',
                    }
                )
                return macd
            case 'trend':
                return base.calculate_ema(datas, self.trend_source, self.trend_length)


class LayeredLogic(base.LayerGeneratorLogicSetting):
    template_name: str = 'scalp_short_macd'
    main: Logic = Logic()

data_req = base.OhlcvStreamDataRequest(timeframe='5m')

class InputSetting(base.GeneratorInputSetting):
    request: base.OhlcvStreamDataRequest


class layeredInput(base.LayerGeneratorInputSetting):
    main: InputSetting = InputSetting(request=data_req)

output_settings = base.GeneratorOutputSetting(
    signal_type=base.SignalType.Short,
    analysis_style=base.AnalysisStyle.Technical,
    optimizer_tag=base.OptimizerTag.Direct,
    consumption_pattern=base.ConsumptionPattern.Disposable,
    signal_mode=base.SignalMode.Analysis,
    expire_configs=base.ExpireConfigs(
        configs={
            'timedelta': 24 * 60  # one day
        }
    )
)

logic = LayeredLogic()
input_ = layeredInput()

Settings = base.GeneratorSettings.safe_creation(
    template_name='scalp_short_macd',
    logic=logic,
    input_=input_,
    output=output_settings
)
