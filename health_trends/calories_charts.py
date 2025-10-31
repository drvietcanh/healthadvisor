"""
Calories Charts - Biểu đồ cân bằng calories
===========================================

Biểu đồ calories ăn vào vs đốt cháy
"""
import plotly.graph_objects as go
import pandas as pd


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

