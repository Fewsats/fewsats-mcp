from mcp.server.fastmcp import FastMCP
from fewsats.core import Fewsats
import os

# Create FastMCP and Fewsats instances
mcp = FastMCP("Fewsats MCP Server")


def handle_response(response):
    try: return response.status_code, response.json()
    except: return response.status_code, response.text


@mcp.tool()
async def balance() -> str:
    """Retrieve the balance of the user's wallet.
    You will rarely need to call this unless instructed by the user, or to troubleshoot payment issues.
    Fewsats will automatically add balance when needed."""
    return handle_response(Fewsats().balance())

@mcp.tool()
async def payment_methods() -> str:
    """Retrieve the user's payment methods.
    You will rarely need to call this unless instructed by the user, or to troubleshoot payment issues.
    Fewsats will automatically select the best payment method."""
    return handle_response(Fewsats().payment_methods())

@mcp.tool()
async def pay_offer(offer_id: str, l402_offer: dict) -> str:
    """Pays an offer_id from the l402_offers.

    The l402_offer parameter must be a dict with this structure:
    {
        'offers': [
            {
                'offer_id': 'test_offer_2',  # String identifier for the offer
                'amount': 1,                 # Numeric cost value
                'currency': 'usd',           # Currency code
                'description': 'Test offer', # Text description
                'title': 'Test Package'      # Title of the package
            }
        ],
        'payment_context_token': '60a8e027-8b8b-4ccf-b2b9-380ed0930283',  # Payment context token
        'payment_request_url': 'https://api.fewsats.com/v0/l402/payment-request',  # Payment URL
        'version': '0.2.2'  # API version
    }

    Returns payment status response. 
    If payment status is `needs_review` inform the user he will have to approve it at app.fewsats.com"""
    return handle_response(Fewsats().pay_offer(offer_id, l402_offer))

@mcp.tool()
async def payment_info(pid: str) -> str:
    """Retrieve the details of a payment.
    If payment status is `needs_review` inform the user he will have to approve it at app.fewsats.com"""
    return handle_response(Fewsats().payment_info(pid))

@mcp.tool()
async def billing_info() -> str:
    """Retrieve the user's billing information.
    Returns billing details including name, address, and other relevant information.
    This information can also be used as shipping address for purchases."""
    return handle_response(Fewsats().billing_info())


def main():
    mcp.run(transport='stdio')
