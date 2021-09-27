from script import main, show_report

EXPECTED_SAMPLE_OUTPUT = """
polarity | subjectivity | text
--------------------------------------------------
-1.0     | 1.0          | that food was disgusting
-0.7     | 0.667        | I am listening to bad music
-0.3     | 0.3          | this sucks
-0.292   | 0.542        | I found it hard
0.0      | 0.0          | it was so so
0.0      | 0.1          | why is the sky blue?
0.1      | 0.3          | I woke up early today
0.5      | 0.5          | I can do better
0.7      | 0.6          | I am listening to good music
0.7      | 0.8          | I loved that movie
1.0      | 1.0          | this was marvelous
"""


def test_main(capfd):
    scores = main("sample.txt")
    show_report(scores)
    actual = capfd.readouterr().out.strip()
    expected = EXPECTED_SAMPLE_OUTPUT.strip()
    assert actual == expected
