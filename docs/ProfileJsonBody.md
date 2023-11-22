# ProfileJsonBody

## Properties

| Name                      | Type     | Description                                                                                                                                     | Notes      |
| ------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **gender**                | **str**  | The sex of the user; (MALE/FEMALE/NA).                                                                                                          | [optional] |
| **birthday**              | **date** | The date of birth in the format of yyyy-MM-dd.                                                                                                  | [optional] |
| **height**                | **str**  | The height in the format X.XX in the unit system that corresponds to the Accept-Language header provided.                                       | [optional] |
| **about_me**              | **str**  | This is a short description of user.                                                                                                            | [optional] |
| **fullname**              | **str**  | The fullname of the user.                                                                                                                       | [optional] |
| **country**               | **str**  | The country of the user&#x27;s residence. This is a two-character code.                                                                         | [optional] |
| **state**                 | **str**  | The US state of the user&#x27;s residence. This is a two-character code if the country was or is set to US.                                     | [optional] |
| **city**                  | **str**  | The US city of the user&#x27;s residence.                                                                                                       | [optional] |
| **stride_length_walking** | **str**  | Walking stride length in the format X.XX, where it is in the unit system that corresponds to the Accept-Language header provided.               | [optional] |
| **stride_length_running** | **str**  | Running stride length in the format X.XX, where it is in the unit system that corresponds to the Accept-Language header provided.               | [optional] |
| **weight_unit**           | **str**  | Default weight unit on website (which doesn&#x27;t affect API); one of (en_US, en_GB, &#x27;any&#x27; for METRIC).                              | [optional] |
| **height_unit**           | **str**  | Default height/distance unit on website (which doesn&#x27;t affect API); one of (en_US, en_GB, &#x27;any&#x27; for METRIC).                     | [optional] |
| **water_unit**            | **str**  | Default water unit on website (which doesn&#x27;t affect API); one of (en_US, en_GB, &#x27;any&#x27; for METRIC).                               | [optional] |
| **glucose_unit**          | **str**  | Default glucose unit on website (which doesn&#x27;t affect API); one of (en_US, en_GB, &#x27;any&#x27; for METRIC).                             | [optional] |
| **timezone**              | **str**  | The timezone in the format &#x27;America/Los_Angeles&#x27;.                                                                                     | [optional] |
| **foods_locale**          | **str**  | The food database locale in the format of xx.XX.                                                                                                | [optional] |
| **locale**                | **str**  | The locale of the website (country/language); one of the locales, currently – (en_US, fr_FR, de_DE, es_ES, en_GB, en_AU, en_NZ, ja_JP).         | [optional] |
| **locale_lang**           | **str**  | The Language in the format &#x27;xx&#x27;. You should specify either locale or both - localeLang and localeCountry (locale is higher priority). | [optional] |
| **locale_country**        | **str**  | The Country in the format &#x27;xx&#x27;. You should specify either locale or both - localeLang and localeCountry (locale is higher priority).  | [optional] |
| **start_day_of_week**     | **str**  | The Start day of the week, meaning what day the week should start on. Either Sunday or Monday.                                                  | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
