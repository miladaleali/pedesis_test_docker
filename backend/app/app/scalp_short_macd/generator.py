from pedesis.components.signal_generator import templates as generators
from pedesis.components.signal_generator.templates import base
from pedesis.components.stream_processor.models import StreamProcessorSettings
from pedesis.conf.global_settings import EngineSettings

from . import generator_settings as settings

class ScalpShortMacd(base.Generator):
    EXPECTED_INVESTMENT_TIME = 30
    SETTINGS = settings.Settings
    TIMEFRAME: str = '5m'

    def __init__(
        self,
        settings: StreamProcessorSettings = None,
        engine_settings: EngineSettings = None
    ) -> None:
        super().__init__(settings, engine_settings)

        # indicators
        self.macd: base.pd.DataFrame = None
        self.trend: base.pd.Series = None
        self.zeros = base.pd.Series(base.np.zeros(10))

        # datas
        self.main_data: base.pd.DataFrame = None

    def next_data_telegram_msg(self) -> None:
        main_data = f"Main Current Close: {self.main_data.close.iloc[-1]}\nMain Yesterday Close: {self.main_data.close.iloc[-2]}"
        macd = f"MACD Current: {self.macd.iloc[-1]}\nMACD Yesterday: {self.macd.iloc[-2]}"
        trend = f"Trend Current: {self.trend.iloc[-1]}\nTrend Yesterday: {self.trend.iloc[-2]}"
        base.telegram_channel.send_message(f"Generator {self.settings.dbid} Info:\n{main_data}\n{macd}\n{trend}")

    def signal_logic(self) -> bool:
        if self.main_data.close.iloc[-1] < self.trend.iloc[-1]:
            return base.speedy_cross(self.macd.histo, self.zeros, False)
        return False
