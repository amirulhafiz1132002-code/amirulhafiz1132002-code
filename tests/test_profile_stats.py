"""Unit tests for the AMRHZ GitHub profile statistics generator."""
import unittest
from defusedxml import ElementTree as ET

from scripts import generate_profile_stats as stats


class ProfileStatsTests(unittest.TestCase):
    def test_tiny_language_share_is_not_displayed_as_zero(self):
        self.assertEqual(stats.format_percentage(0.04), "<0.1%")

    def test_small_language_share_keeps_two_decimal_places(self):
        self.assertEqual(stats.format_percentage(0.42), "0.42%")

    def test_regular_language_share_keeps_one_decimal_place(self):
        self.assertEqual(stats.format_percentage(48.16), "48.2%")

    def test_zero_language_share_is_explicit(self):
        self.assertEqual(stats.format_percentage(0), "0.0%")

    def test_snapshot_timestamp_is_utc(self):
        self.assertRegex(
            stats.snapshot_timestamp(),
            r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2} UTC$",
        )

    def test_repository_count_uses_fetched_public_repository_list(self):
        svg = stats.stats_svg(
            {"public_repos": 999, "followers": 3},
            [{"stargazers_count": 1, "forks_count": 0}],
            "2026-11-05 00:00 UTC",
        )
        self.assertIn(">1</text>", svg)
        self.assertNotIn(">999</text>", svg)

    def test_snapshot_is_visible_in_both_cards(self):
        stamp = "2026-11-05 00:00 UTC"
        stats_card = stats.stats_svg({"followers": 3}, [], stamp)
        language_card = stats.languages_svg({"Python": 100}, stamp)
        self.assertIn(stamp, stats_card)
        self.assertIn(stamp, language_card)

    def test_language_svg_escapes_tiny_percentage_and_is_well_formed_xml(self):
        svg = stats.languages_svg({"JavaScript": 9999, "Shell": 1}, "2026-11-05 00:00 UTC")
        root = ET.fromstring(svg)
        labels = [element.text for element in root.iter() if element.tag.endswith("text")]
        self.assertIn("<0.1%", labels)

    def test_both_generated_cards_are_well_formed_xml(self):
        stamp = "2026-11-05 00:00 UTC"
        stats_card = stats.stats_svg({"followers": 3}, [], stamp)
        language_card = stats.languages_svg({"Python": 100}, stamp)
        ET.fromstring(stats_card)
        ET.fromstring(language_card)


if __name__ == "__main__":
    unittest.main()
