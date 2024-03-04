# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from pathlib import Path
from typing import Any, Mapping, Optional

from promptflow._constants import LINE_TIMEOUT_SEC
from promptflow.executor._service.contracts.base_request import BaseRequest


class InitializationRequest(BaseRequest):
    """Request model for teh batch run initialization."""

    working_dir: Path
    flow_file: Path
    output_dir: Path
    log_path: Optional[str] = None
    connections: Optional[Mapping[str, Any]] = None
    environment_variables: Optional[Mapping[str, Any]] = None
    worker_count: Optional[int] = None
    line_timeout_sec: Optional[int] = LINE_TIMEOUT_SEC


class LineExecutionRequest(BaseRequest):
    """Request model for line execution in the batch run."""

    run_id: str
    line_number: int
    inputs: Mapping[str, Any]


class AggregationRequest(BaseRequest):
    """Request model for executing aggregation nodes in the batch run."""

    run_id: str
    batch_inputs: Mapping[str, Any]
    aggregation_inputs: Mapping[str, Any]
