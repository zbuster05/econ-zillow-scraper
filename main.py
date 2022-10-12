import requests
import os
import urllib.parse

class ZillowZestimateFetcher():
    def __init__(self, PLACES_API_key: str, MAPS_API_key: str):
        self._PLACES_API_key = PLACES_API_key
        self._MAPS_API_key = MAPS_API_key

    def fetch(self, addresses: [str]):
        pass

    def _fetch_places(self, address: str, radius: int = 2) -> [dict]:
        url_safe_address = urllib.parse.query(address)
        address_request = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={url_safe_address}&key=AIzaSyAZPMn0c9TFEauzCAmjA53MA42sf6bj6tM').json()
        if address_request["results"] == []:
            return ""

        addess_location = address_request[0]["geometry"]["location"]
        lat, lng = (address_location["lat"], address_location["lng"])

        
    
    def _fetch_zpid(self, address: str) -> str:
        headers = {
            'authority': 'www.zillowstatic.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }

        params = {
            'q': address,
            'resultTypes': 'allAddress',
            'resultCount': '5',
        }

        response = requests.get('https://www.zillowstatic.com/autocomplete/v3/suggestions/', params=params, headers=headers)
        if response.json()["results"] == []:
            return ""
        else:
            return response.json()["results"][0]["metaData"]["zpid"]

    def _fetch_house_data(self, zpid: str) -> dict:
        cookies = {
            'zguid': '24|%242d58ea98-e632-4bb6-9c7d-662cd7d1c8db',
            'zgsession': '1|28c800b9-9017-4499-9312-018326c3da6f',
            'zjs_user_id': 'null',
            'zg_anonymous_id': '%221a6ed9ed-c188-4237-b11f-edca762289d3%22',
            'zjs_anonymous_id': '%222d58ea98-e632-4bb6-9c7d-662cd7d1c8db%22',
            '_ga': 'GA1.2.2115339018.1664742335',
            'pxcts': '5f2d18aa-4290-11ed-9817-4d644b73654a',
            '_pxvid': '5f2d0afe-4290-11ed-9817-4d644b73654a',
            '_gcl_au': '1.1.822410431.1664742337',
            'DoubleClickSession': 'true',
            '__pdst': '07047eab12744501ab2ea2317d02d35c',
            '_fbp': 'fb.1.1664742337501.2062095787',
            '_cs_c': '0',
            '_pin_unauth': 'dWlkPU1EYzFabVExWXpJdFlUZG1NQzAwTXpjNExUZzBOVFV0TnprNE9URTVZakUyWldZMg',
            'G_ENABLED_IDPS': 'google',
            'utag_main': f"v_id:01839a60e26f001db5931e9a099c05075004d06d00942_sn:1$_se:2$_ss:0$_st:1664745159813$ses_id:1664742384240%3Bexp-session$_pn:2%3Bexp-session",
            '_gid': 'GA1.2.1454021315.1665159590',
            '_gat': '1',
            '_pxff_bsco': '1',
            'JSESSIONID': 'F4E88E5895F77579152BED0DBE8355B6',
            'KruxPixel': 'true',
            '_clck': 'ldi0h3|1|f5i|0',
            '_hp2_ses_props.1215457233': '%7B%22r%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22ts%22%3A1665159592871%2C%22d%22%3A%22www.zillow.com%22%2C%22h%22%3A%22%2Fhow-much-is-my-home-worth%2F%22%7D',
            '_uetsid': 'dfaed710465b11ed81e9730a1991218c',
            '_uetvid': '602cbad0429011ed95f185c3ee2628e8',
            '_hp2_id.1215457233': '%7B%22userId%22%3A%227431330295269196%22%2C%22pageviewId%22%3A%227282166880565767%22%2C%22sessionId%22%3A%223218894318134037%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
            'AWSALB': '9Vk4oQKwGx+0TXdoGsKXSyOAcT5VOi0TFFGowCcCNZMUHn9aS9P/Rjup1Q+w8EVwaoGB+sn9aR1/hnhX47MZrF+X0pASrbSBbOWJ0eZCs33Y25n9qBJ1iFOnZQV1',
            'AWSALBCORS': '9Vk4oQKwGx+0TXdoGsKXSyOAcT5VOi0TFFGowCcCNZMUHn9aS9P/Rjup1Q+w8EVwaoGB+sn9aR1/hnhX47MZrF+X0pASrbSBbOWJ0eZCs33Y25n9qBJ1iFOnZQV1',
            '_cs_id': 'e04c93cd-f940-a367-e2ad-fc74c04ca27a.1664742338.4.1665159599.1665159593.1.1698906338834',
            '_cs_s': '2.5.0.1665161399687',
            '_clsk': 'hk2v51|1665159599961|2|0|b.clarity.ms/collect',
            '_px3': '041408ce0de57bb852a55d521512418de3846c2c0336cefb1b16f0e0791ac0ec:+VgsSOBTMEBoW+aAItTpftbTXyW0/FM2w60COZQtMdzadZQ6ZwKtzcy5yh+N40AFQAqk1G+KCF1osE34zYiniQ==:1000:vUtaIOM9WDIkyZ0Ax/2c9ahsh4T7b1UZB+nQWy5s1IyizJUtyirWL0Mrfdx/GlNSCSkWWFeL9RhAWbnJw+ReCSBVjOnebafvor8SFhQJysE85qynORs0d08uzLbq/9FLmdZfTtx+V0liaC8TnUaLWF1M+kY5Wz/Qw4vPccPl74FU17XP/55dWXDHUwTqAVKwyGuOLyUPRCmN/JsUewXCHg==',
        }

        headers = {
            'authority': 'www.zillow.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'client-id': 'hmimhw-property-search',
            'origin': 'https://www.zillow.com',
            'referer': 'https://www.zillow.com/how-much-is-my-home-worth/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }

        json_data = {
            'operationName': 'HowMuchIsMyHomeWorthReviewQuery',
            'variables': {
                'zpid': zpid,
            },
            'query': 'query HowMuchIsMyHomeWorthReviewQuery($zpid: ID!) {\n  property(zpid: $zpid) {\n    streetAddress\n    city\n    state\n    zipcode\n    bedrooms\n    bathrooms\n    livingArea\n    zestimate\n    homeStatus\n    photos(size: XL) {\n      url\n      __typename\n    }\n    ...OmpHomeWorthUpsell_property\n    isConfirmedClaimedByCurrentSignedInUser\n    isVerifiedClaimedByCurrentSignedInUser\n    ...UARequiredPropertyDimensions_property\n    ...ContactAgentForm_property\n    ...HomeInfo_property\n    __typename\n  }\n  viewer {\n    ...ContactAgentForm_viewer\n    __typename\n  }\n  abTests {\n    ...OmpHomeWorthUpsell_abTests\n    ...UARequiredPropertyDimensions_abTests\n    ...ContactAgentForm_abTests\n    __typename\n  }\n}\n\nfragment OmpHomeWorthUpsell_property on Property {\n  zpid\n  onsiteMessage(placementNames: ["HMIMHWTopSlot"]) {\n    ...onsiteMessage_fragment\n    __typename\n  }\n  __typename\n}\n\nfragment onsiteMessage_fragment on OnsiteMessageResultType {\n  eventId\n  decisionContext\n  messages {\n    skipDisplayReason\n    shouldDisplay\n    isGlobalHoldout\n    isPlacementHoldout\n    placementName\n    testPhase\n    bucket\n    placementId\n    passThrottle\n    lastModified\n    eventId\n    decisionContext\n    selectedTreatment {\n      id\n      name\n      component\n      status\n      renderingProps\n      lastModified\n      __typename\n    }\n    qualifiedTreatments {\n      id\n      name\n      status\n      lastModified\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment OmpHomeWorthUpsell_abTests on ABTests {\n  HMIMHW_ZO_NFS_UPSELL_ONSITE_MESSAGING: abTest(\n    trial: "HMIMHW_ZO_NFS_UPSELL_ONSITE_MESSAGING"\n  )\n  __typename\n}\n\nfragment UARequiredPropertyDimensions_property on Property {\n  currency\n  featuredListingTypeDimension\n  hasPublicVideo\n  hdpTypeDimension\n  listingTypeDimension\n  price\n  propertyTypeDimension\n  standingOffer {\n    isStandingOfferEligible\n    __typename\n  }\n  zpid\n  isZillowOwned\n  zillowOfferMarket {\n    legacyName\n    __typename\n  }\n  ...ShouldShowVideo_property\n  __typename\n}\n\nfragment ShouldShowVideo_property on Property {\n  homeStatus\n  isZillowOwned\n  hasPublicVideo\n  primaryPublicVideo {\n    sources {\n      src\n      __typename\n    }\n    __typename\n  }\n  richMediaVideos {\n    mp4Url\n    hlsUrl\n    __typename\n  }\n  __typename\n}\n\nfragment UARequiredPropertyDimensions_abTests on ABTests {\n  ZO_HDP_HOUR_ONE_VIDEO: abTest(trial: "ZO_HDP_HOUR_ONE_VIDEO")\n  __typename\n}\n\nfragment ContactAgentForm_property on Property {\n  streetAddress\n  state\n  city\n  zipcode\n  zpid\n  homeStatus\n  homeType\n  zestimate\n  homeType\n  isInstantOfferEnabled\n  zillowOfferMarket {\n    name\n    code\n    __typename\n  }\n  __typename\n}\n\nfragment ContactAgentForm_viewer on Viewer {\n  name\n  email\n  zuid\n  __typename\n}\n\nfragment ContactAgentForm_abTests on ABTests {\n  SHOW_PL_LEAD_FORM: abTest(trial: "SHOW_PL_LEAD_FORM")\n  __typename\n}\n\nfragment HomeInfo_property on Property {\n  streetAddress\n  city\n  state\n  zipcode\n  bedrooms\n  bathrooms\n  livingArea\n  homeStatus\n  homeType\n  contingentListingType\n  photos(size: XL) {\n    url\n    __typename\n  }\n  listing_sub_type {\n    is_newHome\n    is_FSBO\n    is_bankOwned\n    is_foreclosure\n    is_forAuction\n    is_comingSoon\n    __typename\n  }\n  __typename\n}\n',
        }

        response = requests.post('https://www.zillow.com/graphql/', cookies=cookies, headers=headers, json=json_data)
        return response.json()

if __name__ == "__main__":
    PLACES_KEY = os.environ.get('GMAPS_PLACES_API_KEY')
    fetcher = ZillowZestimateFetcher(PLACES_KEY, "1")
    print(fetcher._fetch_house_data(fetcher._fetch_zpid("673 Oak Park Way")))
