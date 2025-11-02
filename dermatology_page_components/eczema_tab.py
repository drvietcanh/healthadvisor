"""Eczema Tab Component"""
import streamlit as st
from diseases.dermatology import ECZEMA_INFO

def render_eczema_tab():
    """Tab Chàm Khô"""
    st.header("🌿 Chàm Khô (Eczema/Dermatitis)")
    info = ECZEMA_INFO
    
    with st.expander("📖 Chàm khô là gì?", expanded=True):
        st.markdown(info.get("simple_explanation", ""))
        if "what_happens" in info:
            st.markdown(info["what_happens"])
        if "types" in info:
            st.markdown("\n### Phân loại:")
            for key, type_info in info["types"].items():
                st.markdown(f"**{type_info['name']}:** {type_info['description']}")
                st.caption(f"Thường gặp ở: {', '.join(type_info['common_locations'])}")
                st.divider()
    
    with st.expander("⚠️ Triệu chứng", expanded=False):
        if "symptoms" in info:
            s = info["symptoms"]
            if "common" in s:
                st.markdown("**Dấu hiệu thường gặp:**")
                for x in s["common"]:
                    st.markdown(f"- {x}")
            if "progression" in s:
                st.markdown("\n**Diễn tiến:**")
                for x in s["progression"]:
                    st.markdown(x)
    
    with st.expander("🔍 Nguyên nhân", expanded=False):
        if "causes" in info:
            c = info["causes"]
            if "main" in c:
                for x in c["main"]:
                    st.markdown(f"- {x}")
            if "triggers" in c:
                st.markdown("\n**Yếu tố kích phát:**")
                for x in c["triggers"]:
                    st.markdown(x)
    
    with st.expander("💊 Điều trị", expanded=False):
        if "treatment" in info:
            t = info["treatment"]
            if "home_care" in t:
                h = t["home_care"]
                st.markdown(f"### {h.get('title', '')}")
                for x in h.get("steps", []):
                    st.markdown(x)
                if "duration" in h:
                    st.info(h["duration"])
            
            st.divider()
            if "when_to_see_doctor" in t:
                w = t["when_to_see_doctor"]
                st.markdown(f"### {w.get('title', '')}")
                for x in w.get("reasons", []):
                    st.markdown(x)
            
            st.divider()
            if "doctor_treatment" in t:
                d = t["doctor_treatment"]
                st.markdown(f"### {d.get('title', '')}")
                for x in d.get("options", []):
                    st.markdown(x)
    
    with st.expander("🛡️ Phòng ngừa", expanded=False):
        if "prevention" in info:
            p = info["prevention"]
            st.markdown(f"### {p.get('title', '')}")
            for x in p.get("tips", []):
                st.markdown(x)
    
    if "note" in info:
        st.divider()
        st.warning(info["note"])

