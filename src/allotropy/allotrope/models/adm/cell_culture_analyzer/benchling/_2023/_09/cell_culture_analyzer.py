# generated by datamodel-codegen:
#   filename:  cell-culture-analyzer.schema.json
#   timestamp: 2024-06-04T03:30:28+00:00

from __future__ import annotations

from dataclasses import dataclass

from allotropy.allotrope.models.shared.definitions.custom import (
    TNullableQuantityValueCell,
    TNullableQuantityValueGramPerLiter,
    TNullableQuantityValueMicrometer,
    TNullableQuantityValueMillimeterOfMercury,
    TNullableQuantityValueMillimolePerLiter,
    TNullableQuantityValueMillionCellsPerMilliliter,
    TNullableQuantityValueMilliOsmolesPerKilogram,
    TNullableQuantityValueOpticalDensity,
    TNullableQuantityValuePercent,
    TNullableQuantityValuePH,
    TNullableQuantityValueTODO,
    TNullableQuantityValueUnitPerLiter,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TDateTimeValue,
    TStringValue,
)


@dataclass(kw_only=True)
class DeviceSystemDocument:
    device_identifier: TStringValue | None = None
    model_number: TStringValue | None = None
    device_serial_number: TStringValue | None = None


@dataclass(kw_only=True)
class SampleDocument:
    sample_identifier: TStringValue | None = None
    batch_identifier: TStringValue | None = None
    sample_role_type: str | None = None


@dataclass(kw_only=True)
class AnalyteDocumentItem:
    analyte_name: TStringValue
    molar_concentration: TNullableQuantityValueGramPerLiter | TNullableQuantityValueMillimolePerLiter | TNullableQuantityValueUnitPerLiter | None = (
        None
    )


@dataclass(kw_only=True)
class AnalyteAggregateDocument:
    analyte_document: list[AnalyteDocumentItem] | None = None


@dataclass(kw_only=True)
class MeasurementDocumentItem:
    sample_document: SampleDocument
    measurement_time: TDateTimeValue
    analyte_aggregate_document: AnalyteAggregateDocument
    pco2: TNullableQuantityValueMillimeterOfMercury | None = None
    co2_saturation: TNullableQuantityValuePercent | None = None
    po2: TNullableQuantityValueMillimeterOfMercury | None = None
    o2_saturation: TNullableQuantityValuePercent | None = None
    optical_density: TNullableQuantityValueOpticalDensity | None = None
    pH: TNullableQuantityValuePH | None = None
    osmolality: TNullableQuantityValueMilliOsmolesPerKilogram | None = None
    viability__cell_counter_: TNullableQuantityValuePercent | None = None
    total_cell_density__cell_counter_: TNullableQuantityValueMillionCellsPerMilliliter | None = (
        None
    )
    viable_cell_density__cell_counter_: TNullableQuantityValueMillionCellsPerMilliliter | None = (
        None
    )
    average_live_cell_diameter__cell_counter_: TNullableQuantityValueMicrometer | None = (
        None
    )
    average_total_cell_diameter__cell_counter_: TNullableQuantityValueMicrometer | None = (
        None
    )
    total_cell_diameter_distribution__cell_counter_: TNullableQuantityValueTODO | None = (
        None
    )
    viable_cell_count__cell_counter_: TNullableQuantityValueCell | None = None
    total_cell_count__cell_counter_: TNullableQuantityValueCell | None = None


@dataclass(kw_only=True)
class MeasurementAggregateDocument:
    measurement_identifier: TStringValue
    analyst: TStringValue
    device_system_document: DeviceSystemDocument
    measurement_document: list[MeasurementDocumentItem]
    data_processing_time: TDateTimeValue | None = None


@dataclass(kw_only=True)
class Model:
    manifest: str = "http://purl.allotrope.org/manifests/cell-culture-analyzer/BENCHLING/2023/09/cell-culture-analyzer.manifest"
    measurement_aggregate_document: MeasurementAggregateDocument | None = None