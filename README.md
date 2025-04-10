# fewsats-mcp: A Fewsats MCP Server

[![smithery badge](https://smithery.ai/badge/@Fewsats/fewsats-mcp)](https://smithery.ai/server/@Fewsats/fewsats-mcp)

## Overview

This MCP server integrates with [Fewsats](https://fewsats.com) and allows AI Agents to purchase anything in a secure way.

MCP is


### Tools

1. `balance`
   - Retrieve the balance of the user's wallet
   - Input: None
   - Returns: Current wallet balance information

2. `payment_methods`
   - Retrieve the user's payment methods
   - Input: None
   - Returns: List of available payment methods

3. `pay_offer`
   - Pays an offer with the specified ID from the l402_offers
   - Input:
     - `offer_id` (string): String identifier for the offer
     - `l402_offer` (object): Offer details containing:
       - `offers`: Array of offer objects with ID, amount, currency, description, title
       - `payment_context_token`: Payment context token string
       - `payment_request_url`: URL for payment request
       - `version`: API version string
   - Returns: Payment status response

4. `payment_info`
   - Retrieve the details of a payment
   - Input:
     - `pid` (string): Payment ID to retrieve information for
   - Returns: Detailed payment information


## Installation

### Installing via Smithery

To install Fewsats Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@Fewsats/fewsats-mcp):

```bash
npx -y @smithery/cli install @Fewsats/fewsats-mcp --client claude
```

### Using uv (recommended)

When using [`uv`](https://docs.astral.sh/uv/) no specific installation is needed. We will
use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run *fewsats-mcp*.

```bash
uvx fewsats-mcp
```

### Using PIP

Alternatively you can install `fewsats-mcp` via pip:

```bash
pip install fewsats-mcp
```

After installation, you can run it as a script using:

```bash
fewsats-mcp
```

## Configuration

### Usage with Claude Desktop

Add this to your `claude_desktop_config.json`:

**Important**: Replace `YOUR_FEWSATS_API_KEY` with the API key you obtained from [Fewsats.com](https://fewsats.com/).

<details>
<summary>Using uvx</summary>

```json
"mcpServers": {
  "Fewsats Server": {
    "command": "uvx",
    "args": ["fewsats-mcp"],
    "env": {
      "FEWSATS_API_KEY": "YOUR_FEWSATS_API_KEY"
    }
  }
}
```
</details>
