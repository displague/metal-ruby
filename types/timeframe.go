// Code generated by go-swagger; DO NOT EDIT.

package types

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"github.com/go-openapi/errors"
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
	"github.com/go-openapi/validate"
)

// Timeframe timeframe
//
// swagger:model Timeframe
type Timeframe struct {

	// ended at
	// Required: true
	// Format: date-time
	EndedAt *strfmt.DateTime `json:"ended_at"`

	// started at
	// Required: true
	// Format: date-time
	StartedAt *strfmt.DateTime `json:"started_at"`
}

// Validate validates this timeframe
func (m *Timeframe) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateEndedAt(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateStartedAt(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *Timeframe) validateEndedAt(formats strfmt.Registry) error {

	if err := validate.Required("ended_at", "body", m.EndedAt); err != nil {
		return err
	}

	if err := validate.FormatOf("ended_at", "body", "date-time", m.EndedAt.String(), formats); err != nil {
		return err
	}

	return nil
}

func (m *Timeframe) validateStartedAt(formats strfmt.Registry) error {

	if err := validate.Required("started_at", "body", m.StartedAt); err != nil {
		return err
	}

	if err := validate.FormatOf("started_at", "body", "date-time", m.StartedAt.String(), formats); err != nil {
		return err
	}

	return nil
}

// MarshalBinary interface implementation
func (m *Timeframe) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *Timeframe) UnmarshalBinary(b []byte) error {
	var res Timeframe
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
