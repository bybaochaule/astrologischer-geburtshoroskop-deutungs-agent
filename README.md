# Astrologischer Geburtshoroskop-Deutungs-Agent

Skill-Name: `astrologischer-geburtshoroskop-deutungs-agent`

## Beschreibung

Verwende diesen Skill, um symbolische, reflektierende Geburtshoroskop-Deutungen aus bereitgestellten Geburtsdaten oder Chart-Positionen zu erstellen. Nicht verwenden fuer medizinische, rechtliche, finanzielle, psychologische Krisenberatung oder deterministische Vorhersagen.

## Dateien

```text
astrologischer-geburtshoroskop-deutungs-agent/
|-- SKILL.md
|-- README.md
|-- agents/openai.yaml
|-- assets/
|   |-- birth-data-intake.md
|   `-- reading-output-template.md
|-- references/
|   |-- ethical-guidelines.md
|   |-- interpretation-framework.md
|   `-- style-guide.md
`-- scripts/
    `-- validate_intake.py
```

## Typische Nutzung

- Nutzer liefert Geburtsdaten und möchte eine Geburtshoroskop-Deutung.
- Nutzer liefert bereits berechnete Positionen und möchte eine Synthese.
- Nutzer fragt nach den wichtigsten Mustern in Sonne, Mond, Aszendent, Häusern und Aspekten.
- Nutzer wünscht Reflexionsfragen auf Basis astrologischer Symbolik.

## Nicht-Ziele

- Keine deterministischen Vorhersagen.
- Keine Diagnose, Therapie, Rechts-, Finanz- oder Gesundheitsberatung.
- Keine erfundenen Chart-Details, wenn Daten fehlen.
- Keine Angstmache oder Bindung des Nutzers an eine „Schicksalsdeutung“.

## Beispiel-Prompt

```text
Bitte deute mein Geburtshoroskop symbolisch und nicht deterministisch.
Geburtsdatum: 1992-04-18
Geburtszeit: 07:35
Geburtsort: Koeln, Deutschland
Fokus: Beziehungen, Berufung, emotionale Ressourcen
Falls du keine Positionen berechnen kannst, frage mich nach den berechneten Chart-Daten.
```

## Validierung des Intake-JSON

```bash
python scripts/validate_intake.py ../../../examples/sample-birth-data.json
```
