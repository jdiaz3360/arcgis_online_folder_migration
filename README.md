# ArcGIS Online Folder Migration

A Python script to migrate content from a **specific folder** in one ArcGIS Online organization/account to a **specific folder** in another organization using the **ArcGIS API for Python**.

This script was created as a companion resource for my ArcGIS Online migration tutorial and can be adapted to different ArcGIS Online environments.

## Features

- Connects to a source and destination ArcGIS Online organization.
- Selects content from a specific source folder.
- Creates the destination folder automatically if it does not exist.
- Uses `clone_items()` to migrate ArcGIS Online content.
- Copies data when supported.
- Displays the items found before migration.
- Reports successfully cloned items.
- Captures and displays errors without stopping the entire migration.
- Provides a migration summary when the process is complete.

## Requirements

- Python 3.x
- ArcGIS API for Python
- Access to both the source and destination ArcGIS Online organizations.
- Appropriate privileges to access and clone the selected content.

Install the ArcGIS API for Python using Conda:

```bash
conda install -c esri arcgis
```

For more information about installing the ArcGIS API for Python, see the official Esri documentation.

## Configuration

Open `arcgis_online_folder_migration.py` and modify the configuration section:

```python
SOURCE_URL = "https://source_org.maps.arcgis.com"
SOURCE_USERNAME = "source_username"

DESTINATION_URL = "https://destination_org.maps.arcgis.com"
DESTINATION_USERNAME = "destination_username"

SOURCE_FOLDER = "Source_Folder"
DESTINATION_FOLDER = "Destination_Folder"
```

### Example

```python
SOURCE_URL = "https://myoldorg.maps.arcgis.com"
SOURCE_USERNAME = "my_source_user"

DESTINATION_URL = "https://myneworg.maps.arcgis.com"
DESTINATION_USERNAME = "my_destination_user"

SOURCE_FOLDER = "Production Maps"
DESTINATION_FOLDER = "Migrated Production Maps"
```

## How It Works

The script follows this workflow:

1. Connect to the source ArcGIS Online organization.
2. Connect to the destination ArcGIS Online organization.
3. Locate the specified folder in the source account.
4. Retrieve the items stored in that folder.
5. Check whether the destination folder exists.
6. Create the destination folder when necessary.
7. Clone each source item using `clone_items()`.
8. Place the cloned content in the destination folder.
9. Report successful and failed migrations.
10. Display a migration summary.

## Running the Script

Run the script from a Python environment where the ArcGIS API for Python is installed:

```bash
python arcgis_online_folder_migration.py
```

Depending on your ArcGIS Online authentication configuration, additional authentication may be required.

## Important: Item Dependencies

ArcGIS Online folders are primarily used to **organize content**. They should not be considered self-contained packages.

For example, a Web Map stored in the selected folder may reference:

- Hosted Feature Layers
- Feature Services
- Tables
- Images
- Other Web Maps
- Dashboards
- Web Applications
- External services

Some of these dependencies may be located **outside the selected source folder**.

The ArcGIS API for Python `clone_items()` method can identify and clone many supported dependencies, but you should always review the migrated content and verify that maps, layers, applications, and services work correctly in the destination organization.

## Important: Authentication and Security

**Do not store passwords, tokens, API keys, or other credentials directly in this script, especially if you are using a public GitHub repository.**

Use an authentication method appropriate for your ArcGIS Online organization.

Never commit sensitive credentials to GitHub.

## Before Migrating Production Content

It is strongly recommended to:

1. Test the script with a small folder first.
2. Review the source items and their dependencies.
3. Verify that you have sufficient privileges in both organizations.
4. Confirm that the destination organization has the necessary licenses and capabilities.
5. Validate the cloned content after migration.

## Disclaimer

This script is provided as an educational and administrative example.

ArcGIS Online environments can contain complex dependencies, permissions, sharing settings, groups, applications, hosted services, and organization-specific configurations. Always test migrations before using the script with production content.

## License

This project is licensed under the MIT License.

## Author

**Josue Diaz**

GIS professional focused on ArcGIS, GIS architecture, automation, Python, Web GIS, and geospatial technologies.

### GeoTech con Josue

More ArcGIS, Python, GIS automation, and geospatial technology tutorials are available on my YouTube channel.

---

If this script helped you, consider giving the repository a ⭐.
