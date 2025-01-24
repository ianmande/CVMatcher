from urllib.parse import parse_qs, urlparse

from playwright.async_api import async_playwright


async def extract_job_description(linkedin_url):
    url = ""

    parsed_url = urlparse(linkedin_url)
    query_params = parse_qs(parsed_url.query)

    if "currentJobId" in query_params:
        job_id = query_params["currentJobId"][0]
        url = f"https://www.linkedin.com/jobs/view/{job_id}"
    else:
        url = linkedin_url

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.set_extra_http_headers(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
        )

        await page.goto(url, wait_until="domcontentloaded", timeout=90000)
        await page.wait_for_selector(".show-more-less-html__markup", timeout=15000)
        try:
            await page.click(".show-more-less-html__button--more")
            await page.wait_for_timeout(2000)
        except Exception as e:
            print("extract data", e)
            pass

        job_description = await page.inner_text(".show-more-less-html__markup")

        await browser.close()
        return job_description
