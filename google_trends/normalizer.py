from typing import List, Dict, Any
from datetime import datetime

def normalize_trending_searches(raw_trends: List[Dict[str, str]], country: str) -> List[Dict[str, Any]]:
    """
    Normalize the raw trending searches data into a structured format.
    """
    normalized_trends = []

    for trend in raw_trends:
        try:
            # todo: make .replace("K", "000").replace("M", "000000") more readable
            search_count = trend["searchCount"].replace(",", "").replace("K", "000").replace("M", "000000")
            search_count = int(float(search_count))
        except (ValueError, KeyError):
            search_count = 0

        try:
            trend_percentage = int(trend["searchTrend"].replace("%", ""))
        except (ValueError, KeyError):
            trend_percentage = 0

        # Parse timing information from description
        description = trend.get("description", "")
        is_active = "Active" in description
        duration = 0
        
        # Extract hours ago
        hours_ago = 0
        if "minute" in description:
            minutes = int(description.split()[0])
            hours_ago = minutes / 60
        elif "hour" in description:
            hours_ago = int(description.split()[0])

        normalized_trend = {
            "lang": country.lower(),
            "createdAt": datetime.now().isoformat(),
            "title": trend["title"],
            "searchCount": search_count,
            "trendPercentage": trend_percentage,
            "timing": {
                "hoursAgo": hours_ago,
                "isActive": is_active,
                "duration": duration
            }
        }

        normalized_trends.append(normalized_trend)

    return normalized_trends 