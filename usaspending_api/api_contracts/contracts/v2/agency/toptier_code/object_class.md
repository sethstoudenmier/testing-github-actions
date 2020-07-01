FORMAT: 1A
HOST: https://api.usaspending.gov

# List Object Classes [/api/v2/agency/{toptier_code}/object_class/{?fiscal_year,filter,order,sort,page,limit}]

Returns a list of Object Classes in the Agency's appropriations for a single fiscal year

## GET

+ Request (application/json)
    + Schema

            {
                "$schema": "http://json-schema.org/draft-04/schema#",
                "type": "number"
            }
    + Parameters
        + `toptier_code`: 086 (required, number)
            The toptier code of an agency (could be a CGAC or FREC) so only numeric character strings of length 3-4 are accepted.
        + `fiscal_year` (optional, number)
            The desired appropriations fiscal year. Defaults to the current FY.
        + `filter` (optional, string)
            This will filter the Object Classes by their name to those matching the text.
        + `order` (optional, enum[string])
            Indicates what direction results should be sorted by. Valid options include asc for ascending order or desc for descending order.
            + Default: `desc`
            + Members
                + `desc`
                + `asc`
        + `sort` (optional, enum[string])
            Optional parameter indicating what value results should be sorted by.
            + Default: `obligated_amount`
            + Members
                + `name`
                + `obligated_amount`
                + `gross_outlay_amount`
        + `page` (optional, number)
            The page number that is currently returned.
            + Default: 1
        + `limit` (optional, number)
            How many results are returned.
            + Default: 10

+ Response 200 (application/json)
    + Attributes
        + `toptier_code` (required, string)
        + `fiscal_year` (required, number)
        + `page_metadata` (required, PageMetadata, fixed-type)
            Information used for pagination of results.
        + `results` (required, array[ObjectClass], fixed-type)
        + `messages` (required, array[string], fixed-type)
            An array of warnings or instructional directives to aid consumers of this endpoint with development and debugging.

    + Body

            {
                "toptier_code": "086",
                "fiscal_year": 2020,
                "page_metadata": {
                    "limit": 2,
                    "page": 1,
                    "next": 2,
                    "previous": null,
                    "hasNext": true,
                    "hasPrevious": false,
                    "count": 10
                },
                "results": [
                    {
                        "name": "Grants, subsidies, and contributions",
                        "obligated_amount": 12329194065.31,
                        "gross_outlay_amount": 13196218848.88
                    },
                    {
                        "name": "Full-time permanent",
                        "obligated_amount": 221101112.31,
                        "gross_outlay_amount": 230953611.8
                    }
                ],
                "messages": []
            }

# Data Structures

## ObjectClass (object)
+ `name` (required, string)
+ `obligated_amount` (required, number)
+ `gross_outlay_amount` (required, number)

## PageMetadata (object)
+ `limit` (required, number)
+ `page` (required, number)
+ `next` (required, number, nullable)
+ `previous` (required, number, nullable)
+ `hasNext` (required, boolean)
+ `hasPrevious` (required, boolean)
+ `total` (required, number)