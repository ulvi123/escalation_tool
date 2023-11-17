import opsgenie_sdk

def initialize_opsgenie(api_key):
    conf = opsgenie_sdk.configuration.Configuration()
    conf.api_key['Authorization'] = "db07dbc2-8353-4477-a21d-22c261aea506"  # Replace with your Opsgenie API Key
    api_client = opsgenie_sdk.api_client.ApiClient(configuration=conf)
    alert_api = opsgenie_sdk.AlertApi(api_client=api_client)
    return alert_api


def create_alert(alert_api):
    body = opsgenie_sdk.CreateAlertPayload(
        message='It is a drill and testing of an internal support tool, not an actual outage. ',
        alias='python_sample',
        description='Sample of SDK v2',
        responders=[{'name': 'Streamlit', 'type': 'team'}],
        visible_to=[{'name': 'Streamlit', 'type': 'team'}],
        actions=['Restart', 'AnExampleAction'],
        tags=['OverwriteQuietHours'],
        details={'key1': 'value1', 'key2': 'value2'},
        entity='An example entity',
        priority='P3'
    )
    try:
        create_response = alert_api.create_alert(create_alert_payload=body)
        print(create_response)
        return create_response
    except opsgenie_sdk.ApiException as error:
        print(f'Exception when calling Alert API->create_alert %s\n' % error)


def get_request_status(alert_api, request_id):
    try:
        response =alert_api.get_request_status(request_id=request_id)
        print(response)
        return response
    except opsgenie_sdk.ApiException as error:
        print(f'Exception when calling AlertApi->get_request_status: %s\\n' % error)
