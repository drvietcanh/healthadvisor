"""
Trend Charts - Biểu đồ xu hướng cơ bản
========================================

Tạo biểu đồ xu hướng với đường tham chiếu
"""
import plotly.graph_objects as go
import pandas as pd


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

