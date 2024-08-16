from dataclasses import dataclass

import pandas as pd

from allotropy.parsers.appbio_quantstudio_designandanalysis.appbio_quantstudio_designandanalysis_contents import (
    DesignQuantstudioContents,
)
from allotropy.parsers.appbio_quantstudio_designandanalysis.structure.generic.structure import (
    WellList,
)


@dataclass(frozen=True)
class RelativeStandardCurveWellList(WellList):
    @classmethod
    def get_well_result_data(cls, contents: DesignQuantstudioContents) -> pd.DataFrame:
        new_data = cls._add_data(
            data=contents.get_non_empty_sheet(cls.get_data_sheet()),
            extra_data=contents.get_non_empty_sheet("Replicate Group Result"),
            columns=[
                "Cq SE",
            ],
        )

        return cls._add_data(
            new_data,
            extra_data=contents.get_non_empty_sheet("RQ Replicate Group Result"),
            columns=[
                "EqCq Mean",
                "Adjusted EqCq Mean",
                "Delta EqCq Mean",
                "Delta EqCq SD",
                "Delta EqCq SE",
                "Delta Delta EqCq",
                "Rq",
                "Rq Min",
                "Rq Max",
            ],
        )