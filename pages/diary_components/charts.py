"""
Charts - Biểu đồ và thống kê
"""
import streamlit as st
import plotly.graph_objects as go


def render_charts(df):
    """Hiển thị biểu đồ"""
    st.markdown("#### 📈 Xu hướng theo thời gian")
    
    chart_type = st.selectbox("Chọn chỉ số muốn xem:",
        ["❤️ Huyết áp", "🩸 Đường huyết", "⚖️ Cân nặng", "📊 Tất cả"])
    
    if chart_type == "❤️ Huyết áp":
        _render_bp_chart(df)
    elif chart_type == "🩸 Đường huyết":
        _render_glucose_chart(df)
    elif chart_type == "⚖️ Cân nặng":
        _render_weight_chart(df)
    else:
        _render_all_charts(df)


def _render_bp_chart(df):
    """Biểu đồ huyết áp"""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Ngày giờ'], y=df['Huyết áp tâm thu'],
        mode='lines+markers', name='Tâm thu', line=dict(color='red', width=2), marker=dict(size=8)))
    fig.add_trace(go.Scatter(x=df['Ngày giờ'], y=df['Huyết áp tâm trương'],
        mode='lines+markers', name='Tâm trương', line=dict(color='blue', width=2), marker=dict(size=8)))
    fig.add_hline(y=140, line_dash="dash", line_color="orange", annotation_text="Ngưỡng cao (140)")
    fig.add_hline(y=90, line_dash="dash", line_color="orange", annotation_text="Ngưỡng cao (90)")
    fig.update_layout(title="Biểu đồ Huyết áp", xaxis_title="Thời gian", 
        yaxis_title="Huyết áp (mmHg)", height=500, hovermode='x unified')
    st.plotly_chart(fig, use_container_width=True)


def _render_glucose_chart(df):
    """Biểu đồ đường huyết"""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Ngày giờ'], y=df['Đường huyết (mmol/L)'],
        mode='lines+markers', name='Đường huyết', line=dict(color='green', width=2), marker=dict(size=8)))
    fig.add_hrect(y0=3.9, y1=6.1, fillcolor="green", opacity=0.1, 
        annotation_text="Bình thường (3.9-6.1)", annotation_position="top left")
    fig.add_hrect(y0=6.1, y1=7.0, fillcolor="yellow", opacity=0.1,
        annotation_text="Tiền tiểu đường (6.1-7.0)", annotation_position="top left")
    fig.add_hline(y=7.0, line_dash="dash", line_color="red", annotation_text="Tiểu đường (>7.0)")
    fig.update_layout(title="Biểu đồ Đường huyết", xaxis_title="Thời gian",
        yaxis_title="Đường huyết (mmol/L)", height=500, hovermode='x unified')
    st.plotly_chart(fig, use_container_width=True)


def _render_weight_chart(df):
    """Biểu đồ cân nặng"""
    if 'Cân nặng (kg)' in df.columns:
        df_weight = df[df['Cân nặng (kg)'].notna()]
        if len(df_weight) > 0:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df_weight['Ngày giờ'], y=df_weight['Cân nặng (kg)'],
                mode='lines+markers', name='Cân nặng', line=dict(color='purple', width=2), marker=dict(size=8)))
            fig.update_layout(title="Biểu đồ Cân nặng", xaxis_title="Thời gian",
                yaxis_title="Cân nặng (kg)", height=500, hovermode='x unified')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("📊 Chưa có dữ liệu cân nặng. Hãy nhập cân nặng khi thêm dữ liệu!")
    else:
        st.info("📊 Chưa có dữ liệu cân nặng.")


def _render_all_charts(df):
    """Hiển thị tất cả biểu đồ"""
    st.info("📊 Hiển thị tất cả biểu đồ - Kéo xuống để xem!")
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=df['Ngày giờ'], y=df['Huyết áp tâm thu'],
            mode='lines+markers', name='Tâm thu', line=dict(color='red')))
        fig1.add_trace(go.Scatter(x=df['Ngày giờ'], y=df['Huyết áp tâm trương'],
            mode='lines+markers', name='Tâm trương', line=dict(color='blue')))
        fig1.update_layout(title="Huyết áp", height=300)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df['Ngày giờ'], y=df['Đường huyết (mmol/L)'],
            mode='lines+markers', name='Đường huyết', line=dict(color='green')))
        fig2.update_layout(title="Đường huyết", height=300)
        st.plotly_chart(fig2, use_container_width=True)


def render_data_table(df):
    """Hiển thị bảng dữ liệu"""
    st.markdown("#### 📋 Tất cả bản ghi")
    st.dataframe(df, use_container_width=True, height=400)
    st.info(f"📊 **Tổng cộng:** {len(df)} bản ghi")


def render_statistics(df):
    """Hiển thị thống kê"""
    st.markdown("#### 📈 Thống kê tổng quan")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("📅 Số ngày theo dõi", len(df))
        st.metric("❤️ Huyết áp TB (Tâm thu)", f"{df['Huyết áp tâm thu'].mean():.0f} mmHg")
    
    with col2:
        st.metric("❤️ Huyết áp TB (Tâm trương)", f"{df['Huyết áp tâm trương'].mean():.0f} mmHg")
        st.metric("🩸 Đường huyết TB", f"{df['Đường huyết (mmol/L)'].mean():.1f} mmol/L")
    
    with col3:
        if 'Cân nặng (kg)' in df.columns:
            weight_data = df['Cân nặng (kg)'].dropna()
            if len(weight_data) > 0:
                st.metric("⚖️ Cân nặng TB", f"{weight_data.mean():.1f} kg")
                if len(weight_data) > 1:
                    weight_change = weight_data.iloc[-1] - weight_data.iloc[0]
                    st.metric("📊 Thay đổi cân nặng", f"{weight_change:+.1f} kg", delta=f"{weight_change:+.1f} kg")

