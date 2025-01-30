from django.http import JsonResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.middleware.csrf import get_token
from django.conf import settings
import logging

# Initialize logger
logger = logging.getLogger(__name__)


@csrf_exempt  # Disable CSRF for simplicity since it's a public API
@require_GET  # Only allow GET requests
def get_basic_info(request):
    """
    Public API endpoint that returns basic information in JSON format.
    """
    response_data = {
        # Replace with your registered HNG12 Slack email
        "email": "your-email@example.com",
        "current_datetime": now().isoformat(),
        # Replace with your actual GitHub repo URL
        "github_url": "https://github.com/yourusername/your-repo",
    }

    logger.info("API response generated successfully")
    return JsonResponse(response_data, status=200)


# CORS Handling (If Django-CORS-Headers is installed and configured)
if hasattr(settings, 'CORS_ALLOWED_ORIGINS'):
    from corsheaders.signals import check_request_enabled

    def cors_allow_api(sender, request, **kwargs):
        return request.path.startswith("/api/")

    check_request_enabled.connect(cors_allow_api)
