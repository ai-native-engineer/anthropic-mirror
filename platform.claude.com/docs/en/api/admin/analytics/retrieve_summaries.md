<!-- source: https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries -->

# Get Activity Summaries
GET/v1/organizations/analytics/summaries
Get organization-wide activity summaries for a date range.
Returns one entry per day in [starting_date, ending_date). Data is finalized with a 3-day lag: when ending_date is omitted it defaults to 2 days before today, so the last entry covers the most recent day with finalized data. Available to organizations on a Claude Enterprise plan. Requires an API key with the `read:analytics` scope.
##### Query ParametersExpand Collapse 
starting_date: string
UTC date in YYYY-MM-DD format. Start of the date range (inclusive). Must be at least 3 days in the past (data is finalized with a 3-day lag) and no earlier than 2026-01-01.
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#retrieve_summaries.starting_date)
ending_date: optional string
UTC date in YYYY-MM-DD format. End of the date range (exclusive). Data is finalized with a 3-day lag, so this can be at most 2 days before today — which is also the default when omitted, making the last entry cover the most recent day with finalized data. The range may span at most 366 days.
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#retrieve_summaries.ending_date)
ActivitySummary object { summaries } 
Response for GET /v1/organizations/analytics/summaries.
summaries: array of object { assigned_seat_count, cowork_daily_active_user_count, cowork_monthly_active_user_count, 10 more } 
assigned_seat_count: number
Number of seats currently assigned to members
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#activity_summary.summaries.items.assigned_seat_count)
cowork_daily_active_user_count: number
Number of users with Cowork activity on the requested day
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#activity_summary.summaries.items.cowork_daily_active_user_count)
cowork_monthly_active_user_count: number
Number of users with Cowork activity in the 30-day rolling window
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#activity_summary.summaries.items.cowork_monthly_active_user_count)
cowork_weekly_active_user_count: number
Number of users with Cowork activity in the 7-day rolling window
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#activity_summary.summaries.items.cowork_weekly_active_user_count)
daily_active_user_count: number
Number of users with token consumption on the requested day
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#activity_summary.summaries.items.daily_active_user_count)
daily_adoption_rate: number
Percentage of assigned seats with activity on the requested day (DAU / assigned_seat_count * 100)
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#activity_summary.summaries.items.daily_adoption_rate)
ending_at: string
End time in UTC of aggregation period (e.g. 2026-01-16T00:00
)
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#activity_summary.summaries.items.ending_at)
monthly_active_user_count: number
Number of users with token consumption in the 30-day rolling window
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#activity_summary.summaries.items.monthly_active_user_count)
monthly_adoption_rate: number
Percentage of assigned seats with activity in the 30-day rolling window (MAU / assigned_seat_count * 100)
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#activity_summary.summaries.items.monthly_adoption_rate)
pending_invite_count: number
Number of pending invitations to join the organization
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#activity_summary.summaries.items.pending_invite_count)
starting_at: string
Start time in UTC of aggregation period (e.g. 2026-01-15T00:00
)
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#activity_summary.summaries.items.starting_at)
weekly_active_user_count: number
Number of users with token consumption in the 7-day rolling window
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#activity_summary.summaries.items.weekly_active_user_count)
weekly_adoption_rate: number
Percentage of assigned seats with activity in the 7-day rolling window (WAU / assigned_seat_count * 100)
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#activity_summary.summaries.items.weekly_adoption_rate)
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#activity_summary.summaries)
[](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries#activity_summary)
Get Activity Summaries

curl https://api.anthropic.com/v1/organizations/analytics/summaries \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "summaries": [
      "assigned_seat_count": 0,
      "cowork_daily_active_user_count": 0,
      "cowork_monthly_active_user_count": 0,
      "cowork_weekly_active_user_count": 0,
      "daily_active_user_count": 0,
      "daily_adoption_rate": 0,
      "ending_at": "ending_at",
      "monthly_active_user_count": 0,
      "monthly_adoption_rate": 0,
      "pending_invite_count": 0,
      "starting_at": "starting_at",
      "weekly_active_user_count": 0,
      "weekly_adoption_rate": 0
  ]

  "summaries": [
      "assigned_seat_count": 0,
      "cowork_daily_active_user_count": 0,
      "cowork_monthly_active_user_count": 0,
      "cowork_weekly_active_user_count": 0,
      "daily_active_user_count": 0,
      "daily_adoption_rate": 0,
      "ending_at": "ending_at",
      "monthly_active_user_count": 0,
      "monthly_adoption_rate": 0,
      "pending_invite_count": 0,
      "starting_at": "starting_at",
      "weekly_active_user_count": 0,
      "weekly_adoption_rate": 0
  ]
