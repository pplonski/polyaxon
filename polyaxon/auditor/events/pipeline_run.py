import auditor

from event_manager.events import pipeline_run

auditor.subscribe(pipeline_run.PipelineRunCreatedEvent)
auditor.subscribe(pipeline_run.PipelineRunUpdatedEvent)
auditor.subscribe(pipeline_run.PipelineRunCleanedTriggeredEvent)
auditor.subscribe(pipeline_run.PipelineRunViewedEvent)
auditor.subscribe(pipeline_run.PipelineRunArchivedEvent)
auditor.subscribe(pipeline_run.PipelineRunRestoredEvent)
auditor.subscribe(pipeline_run.PipelineRunDeletedEvent)
auditor.subscribe(pipeline_run.PipelineRunDeletedTriggeredEvent)
auditor.subscribe(pipeline_run.PipelineRunStoppedEvent)
auditor.subscribe(pipeline_run.PipelineRunStoppedTriggeredEvent)
auditor.subscribe(pipeline_run.PipelineRunResumedEvent)
auditor.subscribe(pipeline_run.PipelineRunResumedTriggeredEvent)
auditor.subscribe(pipeline_run.PipelineRunRestartedEvent)
auditor.subscribe(pipeline_run.PipelineRunRestartedTriggeredEvent)
auditor.subscribe(pipeline_run.PipelineRunSkippedEvent)
auditor.subscribe(pipeline_run.PipelineRunSkippedTriggeredEvent)
auditor.subscribe(pipeline_run.PipelineRunNewStatusEvent)
auditor.subscribe(pipeline_run.PipelineRunSucceededEvent)
auditor.subscribe(pipeline_run.PipelineRunFailedEvent)
auditor.subscribe(pipeline_run.PipelineRunDoneEvent)
