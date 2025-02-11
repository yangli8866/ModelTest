from apis import alerts


class TestGetTelemetryAlert:

    def test_get_telemetry_alert(self):

        res = alerts.Alerts.get_alerts()
        assert res