# -*- coding: utf-8 -*-
# Caliper-python package, constants module
#
# This file is part of the IMS Caliper Analytics(tm) and is licensed to IMS
# Global Learning Consortium, Inc. (http://www.imsglobal.org) under one or more
# contributor license agreements. See the NOTICE file distributed with this
# work for additional information.
#
# IMS Caliper is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, version 3 of the License.
#
# IMS Caliper is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.

CALIPER_VERSION = "v1p2"
CALIPER_CORE_CONTEXT = "http://purl.imsglobal.org/ctx/caliper/{}".format(
    CALIPER_VERSION
)
_CALIPER_PROFILE_CTXTS = (
    "http://purl.imsglobal.org/ctx/caliper/" + CALIPER_VERSION + "/{}"
)
_CALIPER_PROFILE_EXT_CTXTS = _CALIPER_PROFILE_CTXTS + "-extension"


ENTITY_TYPES = {
    "AGENT": "Agent",
    "AGGREGATE_MEASURE": "AggregateMeasure",
    "AGGREGATE_MEASURE_COLLECTION": "AggregateMeasureCollection",
    "AGGREGATE_PROGRESS": "AggregateProgress",
    "AGGREGATE_TIME_ON_TASK": "AggregateTimeOnTask",
    "ANNOTATION": "Annotation",
    "ASSESSMENT": "Assessment",
    "ASSESSMENT_ITEM": "AssessmentItem",
    "ASSIGNABLE_DIGITAL_RESOURCE": "AssignableDigitalResource",
    "ATTEMPT": "Attempt",
    "AUDIO_OBJECT": "AudioObject",
    "BOOKMARK_ANNOTATION": "BookmarkAnnotation",
    "CHAPTER": "Chapter",
    "COLLECTION": "Collection",
    "COMMENT": "Comment",
    "COURSE_OFFERING": "CourseOffering",
    "COURSE_SECTION": "CourseSection",
    "DATE_TIME_QUESTION": "DateTimeQuestion",
    "DATE_TIME_RESPONSE": "DateTimeResponse",
    "DIGITAL_RESOURCE": "DigitalResource",
    "DIGITAL_RESOURCE_COLLECTION": "DigitalResourceCollection",
    "DOCUMENT": "Document",
    "ENTITY": "Entity",
    "EPUB_CHAPTER": "EpubChapter",
    "EPUB_PART": "EpubPart",
    "EPUB_SUB_CHAPTER": "EpubSubChapter",
    "EPUB_VOLUME": "EpubVolume",
    "FILL_IN_BLANK_RESPONSE": "FillinBlankResponse",
    "FORUM": "Forum",
    "FRAME": "Frame",
    "GROUP": "Group",
    "HIGHLIGHT_ANNOTATION": "HighlightAnnotation",
    "IMAGE_OBJECT": "ImageObject",
    "LEARNING_OBJECTIVE": "LearningObjective",
    "LINK": "Link",
    "LIKERT_SCALE": "LikertScale",
    "LTI_LINK": "LtiLink",
    "LTI_SESSION": "LtiSession",
    "MEDIA_LOCATION": "MediaLocation",
    "MEDIA_OBJECT": "MediaObject",
    "MEMBERSHIP": "Membership",
    "MESSAGE": "Message",
    "MULTIPLE_CHOICE_RESPONSE": "MultipleChoiceResponse",
    "MULTIPLE_RESPONSE_RESPONSE": "MultipleResponseResponse",
    "MULTISELECT_QUESTION": "MultiselectQuestion",
    "MULTISELECT_RESPONSE": "MultiselectResponse",
    "MULTISELECT_SCALE": "MultiselectScale",
    "NUMERIC_SCALE": "NumericScale",
    "OPEN_ENDED_QUESTION": "OpenEndedQuestion",
    "OPEN_ENDED_RESPONSE": "OpenEndedResponse",
    "ORGANIZATION": "Organization",
    "PAGE": "Page",
    "PERSON": "Person",
    "QUERY": "Query",
    "QUESTION": "Question",
    "QUESTIONNAIRE": "Questionnaire",
    "QUESTIONNAIRE_ITEM": "QuestionnaireItem",
    "RATING": "Rating",
    "RATING_SCALE_QUESTION": "RatingScaleQuestion",
    "RATING_SCALE_RESPONSE": "RatingScaleResponse",
    "READING": "Reading",
    "RESPONSE": "Response",
    "RESULT": "Result",
    "SCALE": "Scale",
    "SCORE": "Score",
    "SEARCH_RESPONSE": "SearchResponse",
    "SELECT_TEXT_RESPONSE": "SelectTextResponse",
    "SESSION": "Session",
    "SHARED_ANNOTATION": "SharedAnnotation",
    "SOFTWARE_APPLICATION": "SoftwareApplication",
    "SURVEY": "Survey",
    "SURVEY_INVITATION": "SurveyInvitation",
    "SYSTEM_IDENTIFIER": "SystemIdentifier",
    "TAG_ANNOTATION": "TagAnnotation",
    "TEXT_POSITION_SELECTOR": "TextPositionSelector",
    "THREAD": "Thread",
    "TRUE_FALSE_RESPONSE": "TrueFalseResponse",
    "VIDEO_OBJECT": "VideoObject",
    "WEB_PAGE": "WebPage",
}

## map implementing Python classes onto entity types
ENTITY_CLASSES = {
    ENTITY_TYPES[key]: "caliper.entities.{}".format(ENTITY_TYPES[key])
    for key in ENTITY_TYPES.keys()
}


EVENT_TYPES = {
    "ANNOTATION_EVENT": "AnnotationEvent",
    "ASSESSMENT_EVENT": "AssessmentEvent",
    "ASSESSMENT_ITEM_EVENT": "AssessmentItemEvent",
    "ASSIGNABLE_EVENT": "AssignableEvent",
    "EVENT": "Event",
    "FEEDBACK_EVENT": "FeedbackEvent",
    "FORUM_EVENT": "ForumEvent",
    "MEDIA_EVENT": "MediaEvent",
    "MESSAGE_EVENT": "MessageEvent",
    "NAVIGATION_EVENT": "NavigationEvent",
    "GRADE_EVENT": "GradeEvent",
    "QUESTIONNAIRE_EVENT": "QuestionnaireEvent",
    "QUESTIONNAIRE_ITEM_EVENT": "QuestionnaireItemEvent",
    "RESOURCE_MANAGEMENT_EVENT": "ResourceManagementEvent",
    "SEARCH_EVENT": "SearchEvent",
    "SESSION_EVENT": "SessionEvent",
    "SURVEY_EVENT": "SurveyEvent",
    "SURVEY_INVITATION_EVENT": "SurveyInvitationEvent",
    "THREAD_EVENT": "ThreadEvent",
    "TOOL_LAUNCH_EVENT": "ToolLaunchEvent",
    "TOOL_USE_EVENT": "ToolUseEvent",
    "VIEW_EVENT": "ViewEvent",
}

EVENT_CLASSES = {
    EVENT_TYPES[key]: "caliper.events.{}".format(EVENT_TYPES[key])
    for key in EVENT_TYPES.keys()
}

CALIPER_TYPES = {}
CALIPER_TYPES.update(ENTITY_TYPES)
CALIPER_TYPES.update(EVENT_TYPES)

## maps types to Python classnames
CALIPER_CLASSES = {}
CALIPER_CLASSES.update(ENTITY_CLASSES)
CALIPER_CLASSES.update(EVENT_CLASSES)

## maps Python classnames back to types
CALIPER_TYPES_FOR_CLASSES = {
    CALIPER_CLASSES[key]: key for key in CALIPER_CLASSES.keys()
}

## Caliper LTI, Metrics, Roles and Status vocabulary

CALIPER_LTI_MESSAGES = {

    "BASIC_LTI_LAUNCH_REQUEST": "basic-lti-launch-request",
    "CONTENT_ITEM_SELECTION_REQUEST": "ContentItemSelectionRequest",
    "CONTENT_ITEM_SELECTION_RESPONSE": "ContentItemSelection",
    "CONTENT_ITEM_UPDATE_REQUEST": "ContentItemUpdateRequest",
    "RESOURCE_LINK_REQUEST": "LtiResourceLinkRequest",
    "DEEP_LINKING_REQUEST": "LtiDeepLinkingRequest",
    "DEEP_LINKING_RESPONSE": "LtiDeepLinkingResponse",
}

CALIPER_METRICS = {
    "ASSESSMENTS_PASSED": "AssessmentsPassed",
    "ASSESSMENTS_SUBMITTED": "AssessmentsSubmitted",
    "MINUTES_ON_TASK": "MinutesOnTask",
    "SKILLS_MASTERED": "SkillsMastered",
    "STANDARDS_MASTERED": "StandardsMastered",
    "UNITS_COMPLETED": "UnitsCompleted",
    "UNITS_PASSED": "UnitsPassed",
    "WORDS_READ": "WordsRead",
}

CALIPER_ROLES = {
    "ADMINISTRATOR": "Administrator",
    "ADMINISTRATOR_ADMINISTRATOR": "Administrator#Administrator",
    "ADMINISTRATOR_DEVELOPER": "Administrator#Developer",
    "ADMINISTRATOR_EXTERNAL_DEVELOPER": "Administrator#ExternalDeveloper",
    "ADMINISTRATOR_EXTERNAL_SUPPORT": "Administrator#ExternalSupport",
    "ADMINISTRATOR_EXTERNAL_SYSTEM_ADMINISTRATOR": "Administrator#ExternalSystemAdministrator",
    "ADMINISTRATOR_SUPPORT": "Administrator#Support",
    "ADMINISTRATOR_SYSTEM_ADMINISTRATOR": "Administrator#SystemAdministrator",
    "CONTENT_DEVELOPER": "ContentDeveloper",
    "CONTENT_DEVELOPER_CONTENT_DEVELOPER": "ContentDeveloper#ContentDeveloper",
    "CONTENT_DEVELOPER_CONTENT_EXPERT": "ContentDeveloper#ContentExpert",
    "CONTENT_DEVELOPER_EXTERNAL_CONTENT_EXPERT": "ContentDeveloper#ExternalContentExpert",
    "CONTENT_DEVELOPER_LIBRARIAN": "ContentDeveloper#Librarian",
    "INSTRUCTOR": "Instructor",
    "INSTRUCTOR_EXTERNAL_INSTRUCTOR": "Instructor#ExternalInstructor",
    "INSTRUCTOR_GRADER": "Instructor#Grader",
    "INSTRUCTOR_GUEST_INSTRUCTOR": "Instructor#GuestInstructor",
    "INSTRUCTOR_INSTRUCTOR": "Instructor#Instructor",
    "INSTRUCTOR_LECTURER": "Instructor#Lecturer",
    "INSTRUCTOR_PRIMARY_INSTRUCTOR": "Instructor#PrimaryInstructor",
    "INSTRUCTOR_SECONDARY_INSTRUCTOR": "Instructor#SecondaryInstructor",
    "INSTRUCTOR_TEACHING_ASSISTANT": "Instructor#TeachingAssistant",
    "INSTRUCTOR_TEACHING_ASSISTANT_GROUP": "Instructor#TeachingAssistantGroup",
    "INSTRUCTOR_TEACHING_ASSISTANT_OFFERING": "Instructor#TeachingAssistantOffering",
    "INSTRUCTOR_TEACHING_ASSISTANT_SECTION": "Instructor#TeachingAssistantSection",
    "INSTRUCTOR_TEACHING_ASSISTANT_SECTION_ASSOCIATION": "Instructor#TeachingAssistantSectionAssociation",
    "INSTRUCTOR_TEACHING_ASSISTANT_TEMPLATE": "Instructor#TeachingAssistantTemplate",
    "LEARNER": "Learner",
    "EXTERNAL_LEARNER": "Learner#ExternalLearner",
    "GUEST_LEARNER": "Learner#GuestLearner",
    "LEARNER_INSTRUCTOR": "Learner#Instructor",
    "LEARNER_LEARNER": "Learner#Learner",
    "NONCREDIT_LEARNER": "Learner#NonCreditLearner",
    "MANAGER": "Manager",
    "MANAGER_AREA_MANAGER": "Manager#AreaManager",
    "MANAGER_COURSE_COORDINATOR": "Manager#CourseCoordinator",
    "MANAGER_EXTERNAL_OBSERVER": "Manager#ExternalObserver",
    "MANAGER_MANAGER": "Manager#Manager",
    "MANAGER_OBSERVER": "Manager#Observer",
    "MEMBER": "Member",
    "MEMBER_MEMBER": "Member#Member",
    "MENTOR": "Mentor",
    "MENTOR_ADVISOR": "Mentor#Advisor",
    "MENTOR_AUDITOR": "Mentor#Auditor",
    "MENTOR_EXTERNAL_ADVISOR": "Mentor#ExternalAdvisor",
    "MENTOR_EXTERNAL_AUDITOR": "Mentor#ExternalAuditor",
    "MENTOR_EXTERNAL_LEARNING_FACILITATOR": "Mentor#ExternalLearningFacilitator",
    "MENTOR_EXTERNAL_MENTOR": "Mentor#ExternalMentor",
    "MENTOR_EXTERNAL_REVIEWER": "Mentor#ExternalReviewer",
    "MENTOR_EXTERNAL_TUTOR": "Mentor#ExternalTutor",
    "MENTOR_LEARNING_FACILITATOR": "Mentor#LearningFacilitator",
    "MENTOR_MENTOR": "Mentor#Mentor",
    "MENTOR_REVIEWER": "Mentor#Reviewer",
    "MENTOR_TUTOR": "Mentor#Tutor",
    "OFFICER": "Officer",
    "OFFICER_CHAIR": "Officer#Chair",
    "OFFICER_COMMUNICATIONS": "Officer#Communications",
    "OFFICER_SECRETARY": "Officer#Secretary",
    "OFFICER_TREASURER": "Officer#Treasurer",
    "OFFICER_VICE_CHAIR": "Officer#Vice-Chair",
}

CALIPER_STATUS = {
    "ACTIVE": "Active",
    "DELETED": "Deleted",
    "INACTIVE": "Inactive",
}

CALIPER_SYSIDTYPES = {
    "ACCOUNT_USERNAME": "AccountUserName",
    "CASE_ITEM_URI": "CaseItemUri",
    "EMAIL_ADDRESS": "EmailAddress",
    "LIS_SOURCED_ID": "LisSourcedId",
    "LTI_CONTEXT_ID": "LtiContextId",
    "LTI_DEPLOYMENT_ID": "LtiDeploymentId",
    "LTI_PLATFORM_ID": "LtiPlatformId",
    "LTI_TOOL_ID": "LtiToolId",
    "LTI_USERID": "LtiUserId",
    "ONEROSTER_SOURCED_ID": "OneRosterSourcedId",
    "SIS_SOURCEDID": "SisSourcedId",
    "SYSTEM_ID": "SystemId",
    "OTHER": "Other",
}


## Caliper Profiles and their associated properties
CALIPER_PROFILES = {
    "ANNOTATION": "AnnotationProfile",
    "ASSESSMENT": "AssessmentProfile",
    "ASSIGNABLE": "AssignableProfile",
    "FEEDBACK": "FeedbackProfile",
    "FORUM": "ForumProfile",
    "GENERAL": "GeneralProfile",
    "GRADING": "GradingProfile",
    "MEDIA": "MediaProfile",
    "READING": "ReadingProfile",
    "RESOURCE_MANAGEMENT": "ResourceManagementProfile",
    "SEARCH": "SearchProfile",
    "SESSION": "SessionProfile",
    "SURVEY": "SurveyProfile",
    "TOOL_LAUNCH": "ToolLaunchProfile",
    "TOOL_USE": "ToolUseProfile",
}

PROFILE_CONTEXTS = {
    CALIPER_PROFILES[key]: [CALIPER_CORE_CONTEXT] for key in CALIPER_PROFILES.keys()
}

CALIPER_CONTEXTS = {}
CALIPER_CONTEXTS.update(PROFILE_CONTEXTS)

CALIPER_PROFILES_FOR_CONTEXTS = {
    CALIPER_CONTEXTS[key][-1]: key for key in CALIPER_CONTEXTS
}
CALIPER_PROFILES_FOR_CONTEXTS[CALIPER_CORE_CONTEXT] = CALIPER_PROFILES["GENERAL"]

CALIPER_PROFILES_FOR_EVENT_TYPES = {
    EVENT_TYPES["EVENT"]: CALIPER_PROFILES["GENERAL"],
    EVENT_TYPES["ANNOTATION_EVENT"]: CALIPER_PROFILES["ANNOTATION"],
    EVENT_TYPES["ASSESSMENT_EVENT"]: CALIPER_PROFILES["ASSESSMENT"],
    EVENT_TYPES["ASSESSMENT_ITEM_EVENT"]: CALIPER_PROFILES["ASSESSMENT"],
    EVENT_TYPES["ASSIGNABLE_EVENT"]: CALIPER_PROFILES["ASSIGNABLE"],
    EVENT_TYPES["FEEDBACK_EVENT"]: CALIPER_PROFILES["FEEDBACK"],
    EVENT_TYPES["FORUM_EVENT"]: CALIPER_PROFILES["FORUM"],
    EVENT_TYPES["GRADE_EVENT"]: CALIPER_PROFILES["GRADING"],
    EVENT_TYPES["MEDIA_EVENT"]: CALIPER_PROFILES["MEDIA"],
    EVENT_TYPES["MESSAGE_EVENT"]: CALIPER_PROFILES["FORUM"],
    EVENT_TYPES["NAVIGATION_EVENT"]: CALIPER_PROFILES["GENERAL"],
    EVENT_TYPES["QUESTIONNAIRE_EVENT"]: CALIPER_PROFILES["SURVEY"],
    EVENT_TYPES["QUESTIONNAIRE_ITEM_EVENT"]: CALIPER_PROFILES["SURVEY"],
    EVENT_TYPES["RESOURCE_MANAGEMENT_EVENT"]: CALIPER_PROFILES["RESOURCE_MANAGEMENT"],
    EVENT_TYPES["SEARCH_EVENT"]: CALIPER_PROFILES["SEARCH"],
    EVENT_TYPES["SESSION_EVENT"]: CALIPER_PROFILES["SESSION"],
    EVENT_TYPES["SURVEY_EVENT"]: CALIPER_PROFILES["SURVEY"],
    EVENT_TYPES["SURVEY_INVITATION_EVENT"]: CALIPER_PROFILES["SURVEY"],
    EVENT_TYPES["THREAD_EVENT"]: CALIPER_PROFILES["FORUM"],
    EVENT_TYPES["TOOL_LAUNCH_EVENT"]: CALIPER_PROFILES["TOOL_LAUNCH"],
    EVENT_TYPES["TOOL_USE_EVENT"]: CALIPER_PROFILES["TOOL_USE"],
    EVENT_TYPES["VIEW_EVENT"]: CALIPER_PROFILES["GENERAL"],
}

CALIPER_ACTIONS = {
    "ABANDONED": "Abandoned",
    "ACTIVATED": "Activated",
    "ACCEPTED": "Accepted",
    "ADDED": "Added",
    "ARCHIVED": "Archived",
    "ATTACHED": "Attached",
    "BOOKMARKED": "Bookmarked",
    "CHANGED_RESOLUTION": "ChangedResolution",
    "CHANGED_SIZE": "ChangedSize",
    "CHANGED_SPEED": "ChangedSpeed",
    "CHANGED_VOLUME": "ChangedVolume",
    "CLASSIFIED": "Classified",
    "CLOSED_POPOUT": "ClosedPopout",
    "COMMENTED": "Commented",
    "COMPLETED": "Completed",
    "COPIED": "Copied",
    "CREATED": "Created",
    "DEACTIVATED": "Deactivated",
    "DECLINED": "Declined",
    "DELETED": "Deleted",
    "DESCRIBED": "Described",
    "DISABLED_CLOSED_CAPTIONING": "DisabledClosedCaptioning",
    "DISLIKED": "Disliked",
    "DOWNLOADED": "Downloaded",
    "ENABLED_CLOSED_CAPTIONING": "EnabledClosedCaptioning",
    "ENDED": "Ended",
    "ENTERED_FULLSCREEN": "EnteredFullScreen",
    "EXITED_FULLSCREEN": "ExitedFullScreen",
    "FORWARDED_TO": "ForwardedTo",
    "GRADED": "Graded",
    "HID": "Hid",
    "HIGHLIGHTED": "Highlighted",
    "IDENTIFIED": "Identified",
    "JUMPED_TO": "JumpedTo",
    "LAUNCHED": "Launched",
    "LIKED": "Liked",
    "LINKED": "Linked",
    "LOGGED_IN": "LoggedIn",
    "LOGGED_OUT": "LoggedOut",
    "MARKED_AS_READ": "MarkedAsRead",
    "MARKED_AS_UNREAD": "MarkedAsUnread",
    "MODIFIED": "Modified",
    "MUTED": "Muted",
    "NAVIGATED_TO": "NavigatedTo",
    "OPENED_POPOUT": "OpenedPopout",
    "OPTED_IN": "OptedIn",
    "OPTED_OUT": "OptedOut",
    "PAUSED": "Paused",
    "POSTED": "Posted",
    "PRINTED": "Printed",
    "PUBLISHED": "Published",
    "QUESTIONED": "Questioned",
    "RANKED": "Ranked",
    "RECOMMENDED": "Recommended",
    "REMOVED": "Removed",
    "REPLIED": "Replied",
    "RESET": "Reset",
    "RESTARTED": "Restarted",
    "RESTORED": "Restored",
    "RESUMED": "Resumed",
    "RETRIEVED": "Retrieved",
    "REVIEWED": "Reviewed",
    "RETURNED": "Returned",
    "REWOUND": "Rewound",
    "SAVED": "Saved",
    "SEARCHED": "Searched",
    "SENT": "Sent",
    "SHARED": "Shared",
    "SHOWED": "Showed",
    "SKIPPED": "Skipped",
    "STARTED": "Started",
    "SUBMITTED": "Submitted",
    "SUBSCRIBED": "Subscribed",
    "TAGGED": "Tagged",
    "TIMED_OUT": "TimedOut",
    "UNMUTED": "Unmuted",
    "UNPUBLISHED": "Unpublished",
    "UNSUBSCRIBED": "Unsubscribed",
    "UPLOADED": "Uploaded",
    "USED": "Used",
    "VIEWED": "Viewed",
}


GENERAL_EVENT_ACTIONS = list(CALIPER_ACTIONS.values())
ANNOTATION_EVENT_ACTIONS = [
    CALIPER_ACTIONS["BOOKMARKED"],
    CALIPER_ACTIONS["HIGHLIGHTED"],
    CALIPER_ACTIONS["SHARED"],
    CALIPER_ACTIONS["TAGGED"],
]
ASSESSMENT_EVENT_ACTIONS = [
    CALIPER_ACTIONS["PAUSED"],
    CALIPER_ACTIONS["RESTARTED"],
    CALIPER_ACTIONS["RESUMED"],
    CALIPER_ACTIONS["STARTED"],
    CALIPER_ACTIONS["SUBMITTED"],
]
ASSESSMENT_ITEM_EVENT_ACTIONS = [
    CALIPER_ACTIONS["COMPLETED"],
    CALIPER_ACTIONS["SKIPPED"],
    CALIPER_ACTIONS["STARTED"],
]
ASSIGNABLE_EVENT_ACTIONS = [
    CALIPER_ACTIONS["ACTIVATED"],
    CALIPER_ACTIONS["COMPLETED"],
    CALIPER_ACTIONS["DEACTIVATED"],
    CALIPER_ACTIONS["STARTED"],
    CALIPER_ACTIONS["SUBMITTED"],
]
FEEDBACK_EVENT_ACTIONS = [CALIPER_ACTIONS["COMMENTED"], CALIPER_ACTIONS["RANKED"]]
FORUM_EVENT_ACTIONS = [CALIPER_ACTIONS["SUBSCRIBED"], CALIPER_ACTIONS["UNSUBSCRIBED"]]
GRADE_EVENT_ACTIONS = [CALIPER_ACTIONS["GRADED"]]
MEDIA_EVENT_ACTIONS = [
    CALIPER_ACTIONS["CHANGED_RESOLUTION"],
    CALIPER_ACTIONS["CHANGED_SIZE"],
    CALIPER_ACTIONS["CHANGED_SPEED"],
    CALIPER_ACTIONS["CHANGED_VOLUME"],
    CALIPER_ACTIONS["CLOSED_POPOUT"],
    CALIPER_ACTIONS["DISABLED_CLOSED_CAPTIONING"],
    CALIPER_ACTIONS["ENABLED_CLOSED_CAPTIONING"],
    CALIPER_ACTIONS["ENDED"],
    CALIPER_ACTIONS["ENTERED_FULLSCREEN"],
    CALIPER_ACTIONS["EXITED_FULLSCREEN"],
    CALIPER_ACTIONS["FORWARDED_TO"],
    CALIPER_ACTIONS["JUMPED_TO"],
    CALIPER_ACTIONS["MUTED"],
    CALIPER_ACTIONS["OPENED_POPOUT"],
    CALIPER_ACTIONS["PAUSED"],
    CALIPER_ACTIONS["RESUMED"],
    CALIPER_ACTIONS["RESTARTED"],
    CALIPER_ACTIONS["STARTED"],
    CALIPER_ACTIONS["UNMUTED"],
]
MESSAGE_EVENT_ACTIONS = [
    CALIPER_ACTIONS["MARKED_AS_READ"],
    CALIPER_ACTIONS["MARKED_AS_UNREAD"],
    CALIPER_ACTIONS["POSTED"],
]
NAVIGATION_EVENT_ACTIONS = [CALIPER_ACTIONS["NAVIGATED_TO"]]
QUESTIONNAIRE_EVENT_ACTIONS = [
    CALIPER_ACTIONS["COMPLETED"],
    CALIPER_ACTIONS["STARTED"],
    CALIPER_ACTIONS["SUBMITTED"],
]
QUESTIONNAIRE_ITEM_EVENT_ACTIONS = [
    CALIPER_ACTIONS["STARTED"],
    CALIPER_ACTIONS["SKIPPED"],
    CALIPER_ACTIONS["COMPLETED"],
    CALIPER_ACTIONS["SUBMITTED"],
]
RESOURCE_MANAGEMENT_EVENT_ACTIONS = [
    CALIPER_ACTIONS["ARCHIVED"],
    CALIPER_ACTIONS["COPIED"],
    CALIPER_ACTIONS["CREATED"],
    CALIPER_ACTIONS["DELETED"],
    CALIPER_ACTIONS["DESCRIBED"],
    CALIPER_ACTIONS["DOWNLOADED"],
    CALIPER_ACTIONS["MODIFIED"],
    CALIPER_ACTIONS["PRINTED"],
    CALIPER_ACTIONS["PUBLISHED"],
    CALIPER_ACTIONS["RESTORED"],
    CALIPER_ACTIONS["RETRIEVED"],
    CALIPER_ACTIONS["SAVED"],
    CALIPER_ACTIONS["UNPUBLISHED"],
    CALIPER_ACTIONS["UPLOADED"],
]
SEARCH_EVENT_ACTIONS = [CALIPER_ACTIONS["SEARCHED"]]
SESSION_EVENT_ACTIONS = [
    CALIPER_ACTIONS["LOGGED_IN"],
    CALIPER_ACTIONS["LOGGED_OUT"],
    CALIPER_ACTIONS["TIMED_OUT"],
]
SURVEY_EVENT_ACTIONS = [CALIPER_ACTIONS["OPTED_IN"], CALIPER_ACTIONS["OPTED_OUT"]]
SURVEY_INVITATION_EVENT_ACTIONS = [
    CALIPER_ACTIONS["ACCEPTED"],
    CALIPER_ACTIONS["DECLINED"],
    CALIPER_ACTIONS["SENT"],
]
THREAD_EVENT_ACTIONS = [
    CALIPER_ACTIONS["MARKED_AS_READ"],
    CALIPER_ACTIONS["MARKED_AS_UNREAD"],
]
TOOL_LAUNCH_EVENT_ACTIONS = [CALIPER_ACTIONS["LAUNCHED"], CALIPER_ACTIONS["RETURNED"]]
TOOL_USE_EVENT_ACTIONS = [CALIPER_ACTIONS["USED"]]
VIEW_EVENT_ACTIONS = [CALIPER_ACTIONS["VIEWED"]]


CALIPER_PROFILE_ACTIONS = {}
CALIPER_PROFILE_ACTIONS.update(
    {
        CALIPER_PROFILES["GENERAL"]: {
            EVENT_TYPES["EVENT"]: GENERAL_EVENT_ACTIONS,
            EVENT_TYPES["ANNOTATION_EVENT"]: ANNOTATION_EVENT_ACTIONS,
            EVENT_TYPES["ASSESSMENT_EVENT"]: ASSESSMENT_EVENT_ACTIONS,
            EVENT_TYPES["ASSESSMENT_ITEM_EVENT"]: ASSESSMENT_ITEM_EVENT_ACTIONS,
            EVENT_TYPES["ASSIGNABLE_EVENT"]: ASSIGNABLE_EVENT_ACTIONS,
            EVENT_TYPES["FORUM_EVENT"]: FORUM_EVENT_ACTIONS,
            EVENT_TYPES["GRADE_EVENT"]: GRADE_EVENT_ACTIONS,
            EVENT_TYPES["MEDIA_EVENT"]: MEDIA_EVENT_ACTIONS,
            EVENT_TYPES["MESSAGE_EVENT"]: MESSAGE_EVENT_ACTIONS,
            EVENT_TYPES["NAVIGATION_EVENT"]: NAVIGATION_EVENT_ACTIONS,
            EVENT_TYPES["RESOURCE_MANAGEMENT_EVENT"]: RESOURCE_MANAGEMENT_EVENT_ACTIONS,
            EVENT_TYPES["SEARCH_EVENT"]: SEARCH_EVENT_ACTIONS,
            EVENT_TYPES["SESSION_EVENT"]: SESSION_EVENT_ACTIONS,
            EVENT_TYPES["THREAD_EVENT"]: THREAD_EVENT_ACTIONS,
            EVENT_TYPES["TOOL_LAUNCH_EVENT"]: TOOL_LAUNCH_EVENT_ACTIONS,
            EVENT_TYPES["TOOL_USE_EVENT"]: TOOL_USE_EVENT_ACTIONS,
            EVENT_TYPES["VIEW_EVENT"]: VIEW_EVENT_ACTIONS,
        }
    }
)
CALIPER_PROFILE_ACTIONS.update(
    {
        CALIPER_PROFILES["ANNOTATION"]: {
            EVENT_TYPES["ANNOTATION_EVENT"]: ANNOTATION_EVENT_ACTIONS,
            EVENT_TYPES["VIEW_EVENT"]: VIEW_EVENT_ACTIONS,
        }
    }
)
CALIPER_PROFILE_ACTIONS.update(
    {
        CALIPER_PROFILES["ASSESSMENT"]: {
            EVENT_TYPES["ASSESSMENT_EVENT"]: ASSESSMENT_EVENT_ACTIONS,
            EVENT_TYPES["ASSESSMENT_ITEM_EVENT"]: ASSESSMENT_ITEM_EVENT_ACTIONS,
            EVENT_TYPES["NAVIGATION_EVENT"]: NAVIGATION_EVENT_ACTIONS,
            EVENT_TYPES["VIEW_EVENT"]: VIEW_EVENT_ACTIONS,
        }
    }
)
CALIPER_PROFILE_ACTIONS.update(
    {
        CALIPER_PROFILES["ASSIGNABLE"]: {
            EVENT_TYPES["ASSIGNABLE_EVENT"]: ASSIGNABLE_EVENT_ACTIONS,
            EVENT_TYPES["NAVIGATION_EVENT"]: NAVIGATION_EVENT_ACTIONS,
            EVENT_TYPES["VIEW_EVENT"]: VIEW_EVENT_ACTIONS,
        }
    }
)
CALIPER_PROFILE_ACTIONS.update(
    {
        CALIPER_PROFILES["FEEDBACK"]: {
            EVENT_TYPES["FEEDBACK_EVENT"]: FEEDBACK_EVENT_ACTIONS,
        }
    }
)
CALIPER_PROFILE_ACTIONS.update(
    {
        CALIPER_PROFILES["FORUM"]: {
            EVENT_TYPES["FORUM_EVENT"]: FORUM_EVENT_ACTIONS,
            EVENT_TYPES["MESSAGE_EVENT"]: MESSAGE_EVENT_ACTIONS,
            EVENT_TYPES["NAVIGATION_EVENT"]: NAVIGATION_EVENT_ACTIONS,
            EVENT_TYPES["THREAD_EVENT"]: THREAD_EVENT_ACTIONS,
            EVENT_TYPES["VIEW_EVENT"]: VIEW_EVENT_ACTIONS,
        }
    }
)
CALIPER_PROFILE_ACTIONS.update(
    {
        CALIPER_PROFILES["GRADING"]: {
            EVENT_TYPES["GRADE_EVENT"]: GRADE_EVENT_ACTIONS,
            EVENT_TYPES["VIEW_EVENT"]: VIEW_EVENT_ACTIONS,
        }
    }
)
CALIPER_PROFILE_ACTIONS.update(
    {
        CALIPER_PROFILES["MEDIA"]: {
            EVENT_TYPES["MEDIA_EVENT"]: MEDIA_EVENT_ACTIONS,
            EVENT_TYPES["NAVIGATION_EVENT"]: NAVIGATION_EVENT_ACTIONS,
            EVENT_TYPES["VIEW_EVENT"]: VIEW_EVENT_ACTIONS,
        }
    }
)
CALIPER_PROFILE_ACTIONS.update(
    {
        CALIPER_PROFILES["READING"]: {
            EVENT_TYPES["NAVIGATION_EVENT"]: NAVIGATION_EVENT_ACTIONS,
            EVENT_TYPES["VIEW_EVENT"]: VIEW_EVENT_ACTIONS,
        }
    }
)
CALIPER_PROFILE_ACTIONS.update(
    {
        CALIPER_PROFILES["RESOURCE_MANAGEMENT"]: {
            EVENT_TYPES["RESOURCE_MANAGEMENT_EVENT"]: RESOURCE_MANAGEMENT_EVENT_ACTIONS,
        }
    }
)
CALIPER_PROFILE_ACTIONS.update(
    {CALIPER_PROFILES["SEARCH"]: {EVENT_TYPES["SEARCH_EVENT"]: SEARCH_EVENT_ACTIONS,}}
)
CALIPER_PROFILE_ACTIONS.update(
    {
        CALIPER_PROFILES["SESSION"]: {
            EVENT_TYPES["SESSION_EVENT"]: SESSION_EVENT_ACTIONS,
        }
    }
)
CALIPER_PROFILE_ACTIONS.update(
    {
        CALIPER_PROFILES["SURVEY"]: {
            EVENT_TYPES["NAVIGATION_EVENT"]: NAVIGATION_EVENT_ACTIONS,
            EVENT_TYPES["QUESTIONNAIRE_EVENT"]: QUESTIONNAIRE_EVENT_ACTIONS,
            EVENT_TYPES["QUESTIONNAIRE_ITEM_EVENT"]: QUESTIONNAIRE_ITEM_EVENT_ACTIONS,
            EVENT_TYPES["RESOURCE_MANAGEMENT_EVENT"]: RESOURCE_MANAGEMENT_EVENT_ACTIONS,
            EVENT_TYPES["SURVEY_EVENT"]: SURVEY_EVENT_ACTIONS,
            EVENT_TYPES["SURVEY_INVITATION_EVENT"]: SURVEY_INVITATION_EVENT_ACTIONS,
            EVENT_TYPES["VIEW_EVENT"]: VIEW_EVENT_ACTIONS,
        }
    }
)
CALIPER_PROFILE_ACTIONS.update(
    {
        CALIPER_PROFILES["TOOL_LAUNCH"]: {
            EVENT_TYPES["TOOL_LAUNCH_EVENT"]: TOOL_LAUNCH_EVENT_ACTIONS,
        }
    }
)
CALIPER_PROFILE_ACTIONS.update(
    {
        CALIPER_PROFILES["TOOL_USE"]: {
            EVENT_TYPES["TOOL_USE_EVENT"]: TOOL_USE_EVENT_ACTIONS,
        }
    }
)
