from report.forecast_section import forecast_report



from report.executive_sections import (
    executive_summary,
    ai_executive_insights
)

from agent.analytics_engine import (
    get_top_loss_products,
    get_top_states,
    get_top_categories
)

from agent.analytics_engine import (
    get_top_loss_products,
    get_top_states
)
from report.executive_sections import (
    executive_summary,
    ai_executive_insights
)
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    HRFlowable,
    Table,
    TableStyle
)
from agent.analytics_engine import (
    get_top_loss_products
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib import colors


def generate_pdf_report(
    df,
    revenue,
    profit,
    top_category,
    top_region
):

    pdf = SimpleDocTemplate(
        "AutoMind_Report.pdf"
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.textColor = colors.darkblue

    heading_style = styles["Heading1"]
    heading_style.textColor = colors.darkblue

    body_style = styles["BodyText"]

    content = []

    # =====================================
    # PAGE 1 - COVER PAGE
    # =====================================

    content.append(
        Spacer(1, 120)
    )

    content.append(
        Paragraph(
            "🚀 AutoMind Enterprise",
            title_style
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Executive Business Intelligence Report",
            heading_style
        )
    )

    content.append(
        Spacer(1, 30)
    )

    content.append(
        HRFlowable(
            width="100%",
            thickness=3,
            color=colors.darkblue
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "AI-Powered Business Analytics Platform",
            body_style
        )
    )

    content.append(
        Paragraph(
            "Generated Automatically by AutoMind Enterprise",
            body_style
        )
    )

    content.append(PageBreak())

    # =====================================
    # PAGE 2 - EXECUTIVE SUMMARY
    # =====================================

    content.append(
        Paragraph(
            "📊 Executive Summary",
            heading_style
        )
    )
    orders = 5009
    customers = 793

    summary_text = executive_summary(
        revenue,
        profit,
        orders,
        customers
    )

    content.append(
        Spacer(1, 10)
    )

    content.append(
        HRFlowable(
            width="100%",
            thickness=2,
            color=colors.darkblue
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"<b>Total Revenue:</b> ${revenue:,.0f}",
            body_style
        )
    )

    content.append(
        Paragraph(
            f"<b>Total Profit:</b> ${profit:,.0f}",
            body_style
        )
    )

    content.append(
        Paragraph(
            f"<b>Top Revenue Category:</b> {top_category}",
            body_style
        )
    )

    content.append(
        Paragraph(
            f"<b>Most Profitable Region:</b> {top_region}",
            body_style
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            summary_text,
            body_style
        )
    )

    content.append(PageBreak())
    # =====================================
    # PAGE 3 - KPI DASHBOARD
    # =====================================

    content.append(
        Paragraph(
            "📈 KPI Dashboard",
            heading_style
        )
    )

    content.append(
        Spacer(1, 20)
    )

    kpi_data = [
        ["Metric", "Value"],
        ["Revenue", f"${revenue:,.0f}"],
        ["Profit", f"${profit:,.0f}"],
        ["Orders", "5,009"],
        ["Customers", "793"]
    ]

    table = Table(
        kpi_data,
        colWidths=[200, 200]
    )

    table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
        ])
    )

    content.append(table)

    content.append(PageBreak())

    # =====================================
    # PAGE 4 - MANAGEMENT RECOMMENDATIONS
    # =====================================

    content.append(
        Paragraph(
            "🎯 Management Recommendations",
            heading_style
        )
    )

    content.append(
        Spacer(1, 10)
    )

    content.append(
        HRFlowable(
            width="100%",
            thickness=2,
            color=colors.darkblue
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "1. Focus investment on high-performing categories.",
            body_style
        )
    )

    content.append(
        Paragraph(
            "2. Expand successful operations in profitable regions.",
            body_style
        )
    )

    content.append(
        Paragraph(
            "3. Investigate products and states generating losses.",
            body_style
        )
    )

    content.append(
        Paragraph(
            "4. Use forecasting models to support future planning.",
            body_style
        )
    )

    content.append(
        Paragraph(
            "5. Monitor profitability trends continuously using AutoMind.",
            body_style
        )
    )

    content.append(
        Spacer(1, 30)
    )

    content.append(
        Paragraph(
            "Prepared by AutoMind Enterprise AI",
            heading_style
        )
    )
    content.append(PageBreak())

    content.append(
        Paragraph(
            "📉 Top Loss Products",
            heading_style
        )
    )

    content.append(
        Spacer(1, 20)
    )

    loss_products = get_top_loss_products(df)

    product_data = [
        ["Product", "Profit"]
    ]

    for product, value in loss_products.head(10).items():
        product_data.append(
            [product[:50], f"${value:,.0f}"]
        )

    product_table = Table(
        product_data,
        colWidths=[320, 120]
    )

    product_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])
    )

    content.append(product_table)
    content.append(PageBreak())

    content.append(
        Paragraph(
            "🏆 Top States By Profit",
            heading_style
        )
    )

    content.append(
        Spacer(1, 20)
    )

    top_states = get_top_states(df)

    state_data = [
        ["State", "Profit"]
    ]

    for state, value in top_states.items():

        state_data.append(
            [state, f"${value:,.0f}"]
        )

    state_table = Table(
        state_data,
        colWidths=[250, 150]
    )

    state_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])
    )

    content.append(state_table)
    #start
    content.append(PageBreak())

    content.append(
        Paragraph(
            "💰 Top Categories By Revenue",
            heading_style
        )
    )

    content.append(
        Spacer(1, 20)
    )

    top_categories = get_top_categories(df)

    category_data = [
        ["Category", "Revenue"]
    ]

    for category, value in top_categories.items():

        category_data.append(
            [category, f"${value:,.0f}"]
        )

    category_table = Table(
        category_data,
        colWidths=[250, 150]
    )

    category_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])
    )

    content.append(category_table)
    
    content.append(PageBreak())

    content.append(
        Paragraph(
            "🤖 AI Executive Insights",
            heading_style
        )
    )

    content.append(
        Spacer(1, 20)
    )

    ai_text = ai_executive_insights(
        revenue,
        profit,
        top_category,
        top_region
    )

    content.append(
        Paragraph(
            ai_text,
            body_style
        )
    )

    content.append(PageBreak())

    content.append(
        Paragraph(
            "🔮 Forecast Results",
            heading_style
        )
    )

    content.append(
        Spacer(1, 20)
    )

    forecast_text = forecast_report()

    content.append(
        Paragraph(
            forecast_text,
            body_style
        )
    )

    pdf.build(content)

    return "AutoMind_Report.pdf"