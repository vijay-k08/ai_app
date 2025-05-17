import cv2

def compare_templates(sample_path, template_path, threshold=0.85):
    try:
        sample_img = cv2.imread(sample_path, 0)
        template_img = cv2.imread(template_path, 0)

        if sample_img is None or template_img is None:
            return "Error: Could not read image files."

        res = cv2.matchTemplate(sample_img, template_img, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(res)

        if max_val >= threshold:
            return f"Template match confidence: {max_val:.2f} – Valid"
        else:
            return f"Template match confidence: {max_val:.2f} – Possible tampering"
    except Exception as e:
        return f"Template matching failed: {str(e)}"
