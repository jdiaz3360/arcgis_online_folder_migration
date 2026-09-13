from arcgis.gis import GIS

# ============================================================
# CONFIGURATION
# ============================================================

SOURCE_URL = "https://source_org.maps.arcgis.com"
SOURCE_USERNAME = "source_username"

DESTINATION_URL = "https://destination_org.maps.arcgis.com"
DESTINATION_USERNAME = "destination_username"

SOURCE_FOLDER = "Source_Folder"
DESTINATION_FOLDER = "Destination_Folder"


# ============================================================
# CONNECT TO BOTH ARCGIS ONLINE ORGANIZATIONS
# ============================================================

print("Connecting to the source organization...")
source_gis = GIS(SOURCE_URL, SOURCE_USERNAME)

print("Connecting to the destination organization...")
destination_gis = GIS(DESTINATION_URL, DESTINATION_USERNAME)

print("Connections completed successfully.\n")


# ============================================================
# GET SOURCE USER
# ============================================================

source_user = source_gis.users.get(SOURCE_USERNAME)

if not source_user:
    raise Exception(
        f"Source user '{SOURCE_USERNAME}' could not be found."
    )


# ============================================================
# CHECK IF SOURCE FOLDER EXISTS
# ============================================================

source_folder_exists = False

for folder in source_user.folders:
    if folder["title"].lower() == SOURCE_FOLDER.lower():
        source_folder_exists = True
        break

if not source_folder_exists:
    raise Exception(
        f"Source folder '{SOURCE_FOLDER}' was not found "
        f"for user '{SOURCE_USERNAME}'."
    )

print(f"Source folder found: {SOURCE_FOLDER}")


# ============================================================
# GET ITEMS FROM THE SOURCE FOLDER
# ============================================================

source_items = source_user.items(
    folder=SOURCE_FOLDER,
    max_items=1000
)

if not source_items:
    print("The source folder is empty.")
    raise SystemExit()

print(f"\nItems found: {len(source_items)}\n")

for item in source_items:
    print(
        f"- {item.title} | "
        f"{item.type} | "
        f"{item.id}"
    )


# ============================================================
# CHECK / CREATE DESTINATION FOLDER
# ============================================================

destination_user = destination_gis.users.me

destination_folder_exists = False

for folder in destination_user.folders:
    if folder["title"].lower() == DESTINATION_FOLDER.lower():
        destination_folder_exists = True
        break

if not destination_folder_exists:
    print(
        f"\nCreating destination folder: "
        f"{DESTINATION_FOLDER}"
    )

    destination_gis.content.folders.create(
        DESTINATION_FOLDER
    )
else:
    print(
        f"\nDestination folder already exists: "
        f"{DESTINATION_FOLDER}"
    )


# ============================================================
# CLONE ITEMS
# ============================================================

print("\nStarting migration...\n")

successful_items = []
failed_items = []

for item in source_items:

    print("=" * 70)
    print(f"Processing: {item.title}")
    print(f"Type: {item.type}")
    print(f"Source Item ID: {item.id}")

    try:
        cloned_items = destination_gis.content.clone_items(
            items=[item],
            folder=DESTINATION_FOLDER,
            copy_data=True,
            search_existing_items=False
        )

        if cloned_items:

            for cloned_item in cloned_items:

                print(
                    f"SUCCESS: {cloned_item.title} | "
                    f"{cloned_item.id}"
                )

                successful_items.append({
                    "source_title": item.title,
                    "source_id": item.id,
                    "destination_title": cloned_item.title,
                    "destination_id": cloned_item.id
                })

        else:
            print(
                f"WARNING: No cloned item was returned "
                f"for '{item.title}'."
            )

    except Exception as error:

        print(
            f"ERROR cloning '{item.title}'"
        )

        print(f"Details: {error}")

        failed_items.append({
            "title": item.title,
            "id": item.id,
            "error": str(error)
        })


# ============================================================
# MIGRATION SUMMARY
# ============================================================

print("\n")
print("=" * 70)
print("MIGRATION SUMMARY")
print("=" * 70)

print(
    f"Source items found:     {len(source_items)}"
)

print(
    f"Successfully cloned:    {len(successful_items)}"
)

print(
    f"Failed items:           {len(failed_items)}"
)


if failed_items:

    print("\nItems that could not be cloned:")

    for item in failed_items:

        print(f"- {item['title']}")
        print(f"  Source ID: {item['id']}")
        print(f"  Error: {item['error']}")


print("\nMigration process completed.")
