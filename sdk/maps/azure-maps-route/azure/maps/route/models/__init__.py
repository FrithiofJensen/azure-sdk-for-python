# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import BatchRequest
from ._models import BatchRequestItem
from ._models import BatchResult
from ._models import BatchResultItem
from ._models import BatchResultSummary
from ._models import EffectiveSetting
from ._models import ErrorAdditionalInfo
from ._models import ErrorDetail
from ._models import ErrorResponse
from ._models import GeoJsonFeature
from ._models import GeoJsonFeatureCollection
from ._models import GeoJsonFeatureCollectionData
from ._models import GeoJsonFeatureData
from ._models import GeoJsonGeometry
from ._models import GeoJsonGeometryCollection
from ._models import GeoJsonGeometryCollectionData
from ._models import GeoJsonLineString
from ._models import GeoJsonLineStringData
from ._models import GeoJsonMultiLineString
from ._models import GeoJsonMultiLineStringData
from ._models import GeoJsonMultiPoint
from ._models import GeoJsonMultiPointData
from ._models import GeoJsonMultiPolygon
from ._models import GeoJsonMultiPolygonData
from ._models import GeoJsonObject
from ._models import GeoJsonPoint
from ._models import GeoJsonPointData
from ._models import GeoJsonPolygon
from ._models import GeoJsonPolygonData
from ._models import LatLongPair
from ._models import Route
from ._models import RouteDirectionParameters
from ._models import RouteDirections
from ._models import RouteDirectionsBatchItem
from ._models import RouteDirectionsBatchItemResponse
from ._models import RouteDirectionsBatchResult
from ._models import RouteGuidance
from ._models import RouteInstruction
from ._models import RouteInstructionGroup
from ._models import RouteLeg
from ._models import RouteLegSummary
from ._models import RouteMatrix
from ._models import RouteMatrixQuery
from ._models import RouteMatrixResult
from ._models import RouteMatrixResultResponse
from ._models import RouteMatrixSummary
from ._models import RouteOptimizedWaypoint
from ._models import RouteRange
from ._models import RouteRangeResult
from ._models import RouteReport
from ._models import RouteSection
from ._models import RouteSectionTec
from ._models import RouteSectionTecCause
from ._models import RouteSummary

from ._enums import AlternativeRouteType
from ._enums import ComputeTravelTime
from ._enums import DelayMagnitude
from ._enums import DrivingSide
from ._enums import GeoJsonObjectType
from ._enums import GuidanceInstructionType
from ._enums import GuidanceManeuver
from ._enums import InclineLevel
from ._enums import JsonFormat
from ._enums import JunctionType
from ._enums import Report
from ._enums import ResponseFormat
from ._enums import ResponseSectionType
from ._enums import ResponseTravelMode
from ._enums import RouteAvoidType
from ._enums import RouteInstructionsType
from ._enums import RouteRepresentationForBestOrder
from ._enums import RouteType
from ._enums import SectionType
from ._enums import SimpleCategory
from ._enums import TravelMode
from ._enums import VehicleEngineType
from ._enums import VehicleLoadType
from ._enums import WindingnessLevel
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "BatchRequest",
    "BatchRequestItem",
    "BatchResult",
    "BatchResultItem",
    "BatchResultSummary",
    "EffectiveSetting",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "GeoJsonFeature",
    "GeoJsonFeatureCollection",
    "GeoJsonFeatureCollectionData",
    "GeoJsonFeatureData",
    "GeoJsonGeometry",
    "GeoJsonGeometryCollection",
    "GeoJsonGeometryCollectionData",
    "GeoJsonLineString",
    "GeoJsonLineStringData",
    "GeoJsonMultiLineString",
    "GeoJsonMultiLineStringData",
    "GeoJsonMultiPoint",
    "GeoJsonMultiPointData",
    "GeoJsonMultiPolygon",
    "GeoJsonMultiPolygonData",
    "GeoJsonObject",
    "GeoJsonPoint",
    "GeoJsonPointData",
    "GeoJsonPolygon",
    "GeoJsonPolygonData",
    "LatLongPair",
    "Route",
    "RouteDirectionParameters",
    "RouteDirections",
    "RouteDirectionsBatchItem",
    "RouteDirectionsBatchItemResponse",
    "RouteDirectionsBatchResult",
    "RouteGuidance",
    "RouteInstruction",
    "RouteInstructionGroup",
    "RouteLeg",
    "RouteLegSummary",
    "RouteMatrix",
    "RouteMatrixQuery",
    "RouteMatrixResult",
    "RouteMatrixResultResponse",
    "RouteMatrixSummary",
    "RouteOptimizedWaypoint",
    "RouteRange",
    "RouteRangeResult",
    "RouteReport",
    "RouteSection",
    "RouteSectionTec",
    "RouteSectionTecCause",
    "RouteSummary",
    "AlternativeRouteType",
    "ComputeTravelTime",
    "DelayMagnitude",
    "DrivingSide",
    "GeoJsonObjectType",
    "GuidanceInstructionType",
    "GuidanceManeuver",
    "InclineLevel",
    "JsonFormat",
    "JunctionType",
    "Report",
    "ResponseFormat",
    "ResponseSectionType",
    "ResponseTravelMode",
    "RouteAvoidType",
    "RouteInstructionsType",
    "RouteRepresentationForBestOrder",
    "RouteType",
    "SectionType",
    "SimpleCategory",
    "TravelMode",
    "VehicleEngineType",
    "VehicleLoadType",
    "WindingnessLevel",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
