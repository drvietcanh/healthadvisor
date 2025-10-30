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


def create_calories_balance_chart(df):
    """
    Biểu đồ cân bằng calories (ăn vào vs đốt cháy)
    
    Args:
        df: DataFrame với 'Ngày', 'Calories ăn vào', 'Calories đốt cháy'
    
    Returns:
        Plotly figure
    """
    # Lọc dữ liệu có calories
    df_cal = df[(df['Calories ăn vào'].notna()) | (df['Calories đốt cháy'].notna())].copy()
    
    if len(df_cal) == 0:
        return None
    
    # Fill NaN with 0
    df_cal['Calories ăn vào'] = df_cal['Calories ăn vào'].fillna(0)
    df_cal['Calories đốt cháy'] = df_cal['Calories đốt cháy'].fillna(0)
    df_cal['Cân bằng'] = df_cal['Calories ăn vào'] - df_cal['Calories đốt cháy']
    
    fig = go.Figure()
    
    # Calories ăn vào
    fig.add_trace(go.Bar(
        x=df_cal['Ngày'],
        y=df_cal['Calories ăn vào'],
        name='Ăn vào',
        marker_color='#FF5722',
        hovertemplate='<b>%{x|%d/%m/%Y}</b><br>Ăn vào: %{y} cal<extra></extra>'
    ))
    
    # Calories đốt cháy
    fig.add_trace(go.Bar(
        x=df_cal['Ngày'],
        y=df_cal['Calories đốt cháy'],
        name='Đốt cháy',
        marker_color='#4CAF50',
        hovertemplate='<b>%{x|%d/%m/%Y}</b><br>Đốt cháy: %{y} cal<extra></extra>'
    ))
    
    # Cân bằng (line)
    fig.add_trace(go.Scatter(
        x=df_cal['Ngày'],
        y=df_cal['Cân bằng'],
        name='Cân bằng',
        mode='lines+markers',
        line=dict(color='#2196F3', width=3),
        marker=dict(size=8),
        yaxis='y2',
        hovertemplate='<b>%{x|%d/%m/%Y}</b><br>Cân bằng: %{y:+} cal<extra></extra>'
    ))
    
    # Layout
    fig.update_layout(
        title=dict(
            text='🍽️ Cân Bằng Calories',
            font=dict(size=24, color='#333')
        ),
        xaxis=dict(title='Ngày', showgrid=True, gridcolor='#eee'),
        yaxis=dict(
            title='Calories',
            showgrid=True,
            gridcolor='#eee',
            side='left'
        ),
        yaxis2=dict(
            title='Cân bằng (cal)',
            overlaying='y',
            side='right',
            showgrid=False
        ),
        barmode='group',
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

