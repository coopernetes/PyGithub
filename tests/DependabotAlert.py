from datetime import datetime, timezone

import github.DependabotAlert
import github.PaginatedList

from . import Framework


class DependabotAlert(Framework.TestCase):
    alert: github.DependabotAlert.DependabotAlert

    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("coopernetes/PyGithub")
        self.alert = self.repo.get_dependabot_alert(1)
        self.multiple_alerts = self.repo.get_dependabot_alerts()

    def testAttributes(self):
        self.assertEqual(self.alert.number, 1)
        self.assertEqual(self.alert.state, "dismissed")
        self.assertEqual(self.alert.dependency.package.ecosystem, "pip")
        self.assertEqual(self.alert.dependency.package.name, "jinja2")
        self.assertEqual(self.alert.dependency.manifest_path, "requirements/docs.txt")
        self.assertEqual(self.alert.dependency.scope, "runtime")
        self.assertEqual(self.alert.security_advisory.ghsa_id, "GHSA-h5c8-rqwp-cp95")
        self.assertEqual(self.alert.security_advisory.cve_id, "CVE-2024-22195")
        self.assertEqual(
            self.alert.security_advisory.summary,
            "Jinja vulnerable to HTML attribute injection when passing user input as keys to xmlattr filter",
        )
        self.assertEqual(
            self.alert.security_advisory.description,
            "The `xmlattr` filter in affected versions of Jinja accepts keys containing spaces. XML/HTML attributes cannot contain spaces, as each would then be interpreted as a separate attribute. If an application accepts keys (as opposed to only values) as user input, and renders these in pages that other users see as well, an attacker could use this to inject other attributes and perform XSS. Note that accepting keys as user input is not common or a particularly intended use case of the `xmlattr` filter, and an application doing so should already be verifying what keys are provided regardless of this fix.",
        )
        self.assertEqual(self.alert.security_advisory.severity, "medium")
        self.assertEqual(self.alert.security_advisory.identifiers[0]["value"], "GHSA-h5c8-rqwp-cp95")
        self.assertEqual(self.alert.security_advisory.identifiers[0]["type"], "GHSA")
        self.assertEqual(self.alert.security_advisory.identifiers[1]["value"], "CVE-2024-22195")
        self.assertEqual(self.alert.security_advisory.identifiers[1]["type"], "CVE")
        self.assertEqual(
            self.alert.security_advisory.references[0]["url"],
            "https://github.com/pallets/jinja/security/advisories/GHSA-h5c8-rqwp-cp95",
        )
        self.assertEqual(
            self.alert.security_advisory.references[1]["url"], "https://nvd.nist.gov/vuln/detail/CVE-2024-22195"
        )
        self.assertEqual(
            self.alert.security_advisory.references[2]["url"],
            "https://github.com/pallets/jinja/commit/716795349a41d4983a9a4771f7d883c96ea17be7",
        )
        self.assertEqual(
            self.alert.security_advisory.references[3]["url"], "https://github.com/pallets/jinja/releases/tag/3.1.3"
        )
        self.assertEqual(
            self.alert.security_advisory.references[4]["url"], "https://github.com/advisories/GHSA-h5c8-rqwp-cp95"
        )
        self.assertEqual(
            self.alert.security_advisory.published_at, datetime(2024, 1, 11, 15, 20, 48, tzinfo=timezone.utc)
        )
        self.assertEqual(
            self.alert.security_advisory.updated_at, datetime(2024, 1, 11, 15, 20, 50, tzinfo=timezone.utc)
        )
        self.assertEqual(self.alert.security_advisory.withdrawn_at, None)
        self.assertEqual(self.alert.security_advisory.vulnerabilities[0].package.ecosystem, "pip")
        self.assertEqual(self.alert.security_advisory.vulnerabilities[0].package.name, "jinja2")
        self.assertEqual(self.alert.security_advisory.vulnerabilities[0].vulnerable_version_range, "< 3.1.3")
        self.assertEqual(self.alert.security_advisory.vulnerabilities[0].severity, "medium")
        self.assertEqual(self.alert.security_advisory.vulnerabilities[0].first_patched_version["identifier"], "3.1.3")
        self.assertEqual(self.alert.url, "https://api.github.com/repos/coopernetes/PyGithub/dependabot/alerts/1")
        self.assertEqual(self.alert.html_url, "https://github.com/coopernetes/PyGithub/security/dependabot/1")
        self.assertEqual(self.alert.created_at, datetime(2024, 1, 20, 17, 12, 38, tzinfo=timezone.utc))
        self.assertEqual(self.alert.updated_at, datetime(2024, 1, 20, 22, 4, tzinfo=timezone.utc))
        self.assertEqual(self.alert.dismissed_at, datetime(2024, 1, 20, 22, 4, tzinfo=timezone.utc))
        self.assertEqual(self.alert.dismissed_by.login, "coopernetes")
        self.assertEqual(self.alert.dismissed_reason, "tolerable_risk")
        self.assertEqual(self.alert.dismissed_comment, "Example comment")
        self.assertEqual(self.alert.fixed_at, None)

    def testMultipleAlerts(self):
        self.assertIsInstance(self.multiple_alerts, github.PaginatedList.PaginatedList)
        self.assertIsInstance(self.multiple_alerts[0], github.DependabotAlert.DependabotAlert)
        alert_list = [alert for alert in self.multiple_alerts]
        test_alert = alert_list[0]

        self.assertEqual(len(alert_list), 1)
        # Everything below is the same as testAttributes. This is just to make sure the list works.
        self.assertEqual(test_alert.number, 1)
        self.assertEqual(test_alert.state, "dismissed")
        self.assertEqual(test_alert.dependency.package.ecosystem, "pip")
        self.assertEqual(test_alert.dependency.package.name, "jinja2")
        self.assertEqual(test_alert.dependency.manifest_path, "requirements/docs.txt")
        self.assertEqual(test_alert.dependency.scope, "runtime")
        self.assertEqual(test_alert.security_advisory.ghsa_id, "GHSA-h5c8-rqwp-cp95")
        self.assertEqual(test_alert.security_advisory.cve_id, "CVE-2024-22195")
        self.assertEqual(
            test_alert.security_advisory.summary,
            "Jinja vulnerable to HTML attribute injection when passing user input as keys to xmlattr filter",
        )
        self.assertEqual(
            test_alert.security_advisory.description,
            "The `xmlattr` filter in affected versions of Jinja accepts keys containing spaces. XML/HTML attributes cannot contain spaces, as each would then be interpreted as a separate attribute. If an application accepts keys (as opposed to only values) as user input, and renders these in pages that other users see as well, an attacker could use this to inject other attributes and perform XSS. Note that accepting keys as user input is not common or a particularly intended use case of the `xmlattr` filter, and an application doing so should already be verifying what keys are provided regardless of this fix.",
        )
        self.assertEqual(test_alert.security_advisory.severity, "medium")
        self.assertEqual(test_alert.security_advisory.identifiers[0]["value"], "GHSA-h5c8-rqwp-cp95")
        self.assertEqual(test_alert.security_advisory.identifiers[0]["type"], "GHSA")
        self.assertEqual(test_alert.security_advisory.identifiers[1]["value"], "CVE-2024-22195")
        self.assertEqual(test_alert.security_advisory.identifiers[1]["type"], "CVE")
        self.assertEqual(
            test_alert.security_advisory.published_at, datetime(2024, 1, 11, 15, 20, 48, tzinfo=timezone.utc)
        )
        self.assertEqual(
            test_alert.security_advisory.updated_at, datetime(2024, 1, 11, 15, 20, 50, tzinfo=timezone.utc)
        )
        self.assertEqual(test_alert.security_advisory.withdrawn_at, None)
        self.assertEqual(test_alert.security_advisory.vulnerabilities[0].package.ecosystem, "pip")
        self.assertEqual(test_alert.security_advisory.vulnerabilities[0].package.name, "jinja2")
        self.assertEqual(test_alert.security_advisory.vulnerabilities[0].vulnerable_version_range, "< 3.1.3")
        self.assertEqual(test_alert.security_advisory.vulnerabilities[0].severity, "medium")
        self.assertEqual(test_alert.security_advisory.vulnerabilities[0].first_patched_version["identifier"], "3.1.3")
        self.assertEqual(test_alert.url, "https://api.github.com/repos/coopernetes/PyGithub/dependabot/alerts/1")
        self.assertEqual(test_alert.html_url, "https://github.com/coopernetes/PyGithub/security/dependabot/1")
        self.assertEqual(test_alert.created_at, datetime(2024, 1, 20, 17, 12, 38, tzinfo=timezone.utc))
        self.assertEqual(test_alert.updated_at, datetime(2024, 1, 20, 22, 4, tzinfo=timezone.utc))
        self.assertEqual(test_alert.dismissed_at, datetime(2024, 1, 20, 22, 4, tzinfo=timezone.utc))
        self.assertEqual(test_alert.dismissed_by.login, "coopernetes")
        self.assertEqual(test_alert.dismissed_reason, "tolerable_risk")
        self.assertEqual(test_alert.dismissed_comment, "Example comment")
        self.assertEqual(test_alert.fixed_at, None)

    def testRepr(self):
        self.assertEqual(repr(self.alert), 'DependabotAlert(number=1, ghsa_id="GHSA-h5c8-rqwp-cp95")')