import xml.etree.ElementTree as ET

def parse_sitemap(sitemap_path):
    """
    Parse a sitemap XML file and return a list of URLs.

    Args:
        sitemap_path (str): Path to the sitemap XML file.

    Returns:
        list: List of URLs found in the sitemap.
    """
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()

        # Assuming 'loc' is the tag for URLs; adjust if necessary
        url_list = [elem.text for elem in root.iter() if 'loc' in elem.tag]

        return url_list
    except ET.ParseError as e:
        print(f"Error parsing sitemap at {sitemap_path}: {e}")
        return []

