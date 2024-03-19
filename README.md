# Get me a Roof

This little demo is used to generate requests for job listings on (selected) german flat listing portals using AI.

## Plan

* Interface with Streamlit
  * access restriction?
  * clipboard button
* Query <wg-gesucht.de> or <immoscout.de> and parse the listings
  * optionally with login to see more data
  * send entire html body to page or clean?
* generate answer with some LLM
  * which one?
  * api or hosted? (api probably cheaper)
  * settings to fine-tune text via reprompting / prompt-engineering
