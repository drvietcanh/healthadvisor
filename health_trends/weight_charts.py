"""
Weight Charts - Biểu đồ cân nặng và vòng eo
===========================================

Biểu đồ xu hướng cân nặng và vòng eo để đánh giá béo phì
"""
import plotly.graph_objects as go
import pandas as pd


def create_weight_trend_chart(df):
    """
    Biểu đồ xu hướng cân nặng
    
    Args:
        df: DataFrame với cột 'Ngày' và 'Cân nặng (kg)'
    
    Returns:
        Plotly figure
    """
    # Lọc dữ liệu có cân nặng
    df_weight = df[df['Cân nặng (kg)'].notna()].copy()
    
    if len(df_weight) == 0:
        return None
    
    fig = go.Figure()
    
    # Đường cân nặng
    fig.add_trace(go.Scatter(
        x=df_weight['Ngày'],
        y=df_weight['Cân nặng (kg)'],
        mode='lines+markers',
        name='Cân nặng',
        line=dict(color='#9C27B0', width=3),
        marker=dict(size=10, symbol='circle'),
        fill='tozeroy',
        fillcolor='rgba(156, 39, 176, 0.1)',
        hovertemplate='<b>%{x|%d/%m/%Y}</b><br>Cân nặng: %{y:.1f} kg<extra></extra>'
    ))
    
    # Đường trung bình
    mean_weight = df_weight['Cân nặng (kg)'].mean()
    fig.add_trace(go.Scatter(
        x=df_weight['Ngày'],
        y=[mean_weight] * len(df_weight),
        mode='lines',
        name=f'TB: {mean_weight:.1f} kg',
        line=dict(color='#FF9800', width=2, dash='dash'),
        hovertemplate=f'Trung bình: {mean_weight:.1f} kg<extra></extra>'
    ))
    
    # Layout
    fig.update_layout(
        title=dict(
            text='📊 Xu Hướng Cân Nặng',
            font=dict(size=24, color='#333')
        ),
        xaxis=dict(title='Ngày', showgrid=True, gridcolor='#eee'),
        yaxis=dict(title='Cân nặng (kg)', showgrid=True, gridcolor='#eee'),
        hovermode='x unified',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=14),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=450
    )
    
    return fig


def create_waist_circumference_chart(df):
    """
    Biểu đồ vòng eo (để đánh giá béo phì)
    
    Args:
        df: DataFrame với 'Ngày' và 'Vòng eo (cm)'
    
    Returns:
        Plotly figure
    """
    # Lọc dữ liệu có vòng eo
    df_waist = df[df['Vòng eo (cm)'].notna()].copy()
    
    if len(df_waist) == 0:
        return None
    
    fig = go.Figure()
    
    # Đường vòng eo
    fig.add_trace(go.Scatter(
        x=df_waist['Ngày'],
        y=df_waist['Vòng eo (cm)'],
        mode='lines+markers',
        name='Vòng eo',
        line=dict(color='#FF5722', width=3),
        marker=dict(size=10),
        hovertemplate='<b>%{x|%d/%m/%Y}</b><br>Vòng eo: %{y} cm<extra></extra>'
    ))
    
    # Đường cảnh báo (Nam: 90cm, Nữ: 80cm)
    fig.add_trace(go.Scatter(
        x=df_waist['Ngày'],
        y=[90] * len(df_waist),
        mode='lines',
        name='Ngưỡng Nam (90cm)',
        line=dict(color='#2196F3', width=2, dash='dash'),
        hovertemplate='Ngưỡng Nam: 90 cm<extra></extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=df_waist['Ngày'],
        y=[80] * len(df_waist),
        mode='lines',
        name='Ngưỡng Nữ (80cm)',
        line=dict(color='#E91E63', width=2, dash='dash'),
        hovertemplate='Ngưỡng Nữ: 80 cm<extra></extra>'
    ))
    
    # Layout
    fig.update_layout(
        title=dict(
            text='📏 Xu Hướng Vòng Eo',
            font=dict(size=24, color='#333')
        ),
        xaxis=dict(title='Ngày', showgrid=True, gridcolor='#eee'),
        yaxis=dict(title='Vòng eo (cm)', showgrid=True, gridcolor='#eee'),
        hovermode='x unified',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=14),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=450,
        annotations=[
            dict(
                text="⚠️ Vòng eo cao = Béo bụng = Nguy cơ tim mạch cao",
                xref="paper", yref="paper",
                x=0.5, y=-0.15,
                showarrow=False,
                font=dict(size=12, color='#666')
            )
        ]
    )
    
    return fig

