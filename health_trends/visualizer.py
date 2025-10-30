"""
Visualizer - Vẽ biểu đồ xu hướng đẹp mắt
"""
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

def create_trend_chart(df, metric, title, yaxis_title, reference_lines=None):
    """
    Tạo biểu đồ xu hướng với đường tham chiếu
    
    Args:
        df: DataFrame với cột 'Ngày' và metric
        metric: Tên cột cần vẽ
        title: Tiêu đề biểu đồ
        yaxis_title: Label trục Y
        reference_lines: Dict các đường tham chiếu {'Bình thường': 120, ...}
    
    Returns:
        Plotly figure
    """
    fig = go.Figure()
    
    # Đường xu hướng chính
    fig.add_trace(go.Scatter(
        x=df['Ngày'],
        y=df[metric],
        mode='lines+markers',
        name='Thực tế',
        line=dict(color='#4CAF50', width=3),
        marker=dict(size=8, symbol='circle'),
        hovertemplate='<b>%{x|%d/%m/%Y}</b><br>' + yaxis_title + ': %{y}<extra></extra>'
    ))
    
    # Đường trung bình
    if len(df) > 1:
        mean_value = df[metric].mean()
        fig.add_trace(go.Scatter(
            x=df['Ngày'],
            y=[mean_value] * len(df),
            mode='lines',
            name='Trung bình',
            line=dict(color='#FF9800', width=2, dash='dash'),
            hovertemplate=f'Trung bình: {mean_value:.1f}<extra></extra>'
        ))
    
    # Các đường tham chiếu
    if reference_lines:
        colors = {
            'normal': '#2196F3',
            'warning': '#FF9800',
            'danger': '#F44336'
        }
        
        for label, (value, color_type) in reference_lines.items():
            fig.add_trace(go.Scatter(
                x=df['Ngày'],
                y=[value] * len(df),
                mode='lines',
                name=label,
                line=dict(color=colors.get(color_type, '#999'), width=1, dash='dot'),
                hovertemplate=f'{label}: {value}<extra></extra>'
            ))
    
    # Layout
    fig.update_layout(
        title=dict(
            text=title,
            font=dict(size=24, family='Arial', color='#333')
        ),
        xaxis=dict(
            title='Ngày',
            showgrid=True,
            gridcolor='#eee',
            titlefont=dict(size=16)
        ),
        yaxis=dict(
            title=yaxis_title,
            showgrid=True,
            gridcolor='#eee',
            titlefont=dict(size=16)
        ),
        hovermode='x unified',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=14),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(size=12)
        ),
        height=450
    )
    
    return fig

def create_comparison_chart(current_data, previous_data, metric, title):
    """
    Tạo biểu đồ so sánh tháng này vs tháng trước
    
    Args:
        current_data: DataFrame tháng hiện tại
        previous_data: DataFrame tháng trước
        metric: Metric cần so sánh
        title: Tiêu đề
    
    Returns:
        Plotly figure
    """
    fig = go.Figure()
    
    # Tháng trước
    if previous_data is not None and len(previous_data) > 0:
        fig.add_trace(go.Scatter(
            x=list(range(1, len(previous_data) + 1)),
            y=previous_data[metric],
            mode='lines',
            name='Tháng trước',
            line=dict(color='#999', width=2, dash='dash'),
            opacity=0.6
        ))
    
    # Tháng này
    if current_data is not None and len(current_data) > 0:
        fig.add_trace(go.Scatter(
            x=list(range(1, len(current_data) + 1)),
            y=current_data[metric],
            mode='lines+markers',
            name='Tháng này',
            line=dict(color='#4CAF50', width=3),
            marker=dict(size=6)
        ))
    
    fig.update_layout(
        title=title,
        xaxis=dict(title='Ngày trong tháng'),
        yaxis=dict(title=metric),
        hovermode='x unified',
        plot_bgcolor='white',
        height=400,
        font=dict(size=14)
    )
    
    return fig

def create_correlation_chart(df):
    """
    Tạo biểu đồ tương quan giữa các chỉ số
    (VD: Cân nặng vs Huyết áp)
    
    Args:
        df: DataFrame với nhiều metrics
    
    Returns:
        Plotly figure
    """
    # Kiểm tra cột có sẵn
    if 'Cân nặng (kg)' not in df.columns or 'Huyết áp tâm thu' not in df.columns:
        return None
    
    # Lọc dữ liệu hợp lệ
    df_clean = df[['Cân nặng (kg)', 'Huyết áp tâm thu']].dropna()
    
    if len(df_clean) < 3:
        return None
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df_clean['Cân nặng (kg)'],
        y=df_clean['Huyết áp tâm thu'],
        mode='markers',
        marker=dict(
            size=10,
            color=df_clean['Huyết áp tâm thu'],
            colorscale='RdYlGn_r',
            showscale=True,
            colorbar=dict(title="Huyết áp")
        ),
        text=[f"BP: {bp:.0f}" for bp in df_clean['Huyết áp tâm thu']],
        hovertemplate='Cân nặng: %{x} kg<br>Huyết áp: %{y} mmHg<extra></extra>'
    ))
    
    fig.update_layout(
        title='Mối liên hệ: Cân nặng & Huyết áp',
        xaxis=dict(title='Cân nặng (kg)'),
        yaxis=dict(title='Huyết áp tâm thu (mmHg)'),
        plot_bgcolor='white',
        height=400,
        font=dict(size=14)
    )
    
    return fig

